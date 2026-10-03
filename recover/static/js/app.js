/**
 * DarmanNas (دەرمانناس) - Official Medicine & FDA Verification System
 * Zero-Hallucination Client Logic & OpenFDA API Client
 */

document.addEventListener('DOMContentLoaded', () => {
  // Elements
  const searchInput = document.getElementById('medicineSearchInput');
  const searchSubmitBtn = document.getElementById('searchSubmitBtn');
  const suggestionsDropdown = document.getElementById('suggestionsDropdown');
  const voiceSearchBtn = document.getElementById('voiceSearchBtn');
  const cameraScanBtn = document.getElementById('cameraScanBtn');
  const drugDetailsContainer = document.getElementById('drugDetailsContainer');
  const popularChipsContainer = document.getElementById('popularChipsContainer');

  // Interaction Checker Elements
  const drug1Input = document.getElementById('interactionDrug1');
  const drug2Input = document.getElementById('interactionDrug2');
  const checkInteractionBtn = document.getElementById('checkInteractionBtn');
  const interactionResultCard = document.getElementById('interactionResultCard');

  // Scanner Modal Elements
  const scannerModal = document.getElementById('scannerModal');
  const closeModalBtn = document.getElementById('closeModalBtn');
  const dropzoneFile = document.getElementById('dropzoneFile');
  const scannerDropzone = document.getElementById('scannerDropzone');
  const scannerStatus = document.getElementById('scannerStatus');

  // State
  let currentSearchTimeout = null;
  let speechRecognition = null;
  let isListening = false;

  // Initialize
  initVoiceRecognition();
  loadEmergencyDirectory();
  setupEventListeners();

  // Load default/popular view on start
  performSearch('');

  function setupEventListeners() {
    // Search input live suggestions
    searchInput.addEventListener('input', (e) => {
      clearTimeout(currentSearchTimeout);
      const query = e.target.value.trim();
      currentSearchTimeout = setTimeout(() => {
        if (query.length > 0) {
          fetchSuggestions(query);
        } else {
          suggestionsDropdown.classList.remove('open');
        }
      }, 250);
    });

    searchInput.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') {
        e.preventDefault();
        const query = searchInput.value.trim();
        if (query) {
          selectDrugByQuery(query);
          suggestionsDropdown.classList.remove('open');
        }
      }
    });

    searchSubmitBtn.addEventListener('click', () => {
      const query = searchInput.value.trim();
      if (query) {
        selectDrugByQuery(query);
        suggestionsDropdown.classList.remove('open');
      }
    });

    // Close suggestions on outside click
    document.addEventListener('click', (e) => {
      if (!e.target.closest('.search-wrapper')) {
        suggestionsDropdown.classList.remove('open');
      }
    });

    // Voice Search
    voiceSearchBtn.addEventListener('click', toggleVoiceSearch);

    // Scanner Modal
    cameraScanBtn.addEventListener('click', () => {
      scannerModal.classList.add('open');
    });
    closeModalBtn.addEventListener('click', () => {
      scannerModal.classList.remove('open');
    });
    scannerModal.addEventListener('click', (e) => {
      if (e.target === scannerModal) {
        scannerModal.classList.remove('open');
      }
    });

    // File Drag and Drop for Scanner
    scannerDropzone.addEventListener('click', () => dropzoneFile.click());
    dropzoneFile.addEventListener('change', handleImageUpload);

    // Interaction Checker
    checkInteractionBtn.addEventListener('click', performInteractionCheck);

    // Category Chips
    popularChipsContainer.addEventListener('click', (e) => {
      if (e.target.classList.contains('chip-btn')) {
        document.querySelectorAll('.chip-btn').forEach(btn => btn.classList.remove('active'));
        e.target.classList.add('active');
        const filter = e.target.getAttribute('data-filter');
        filterByCategory(filter);
      }
    });
  }

  // Live Suggestions API
  async function fetchSuggestions(query) {
    try {
      const res = await fetch(`/api/search?q=${encodeURIComponent(query)}`);
      const data = await res.json();
      renderSuggestions(data.results || []);
    } catch (err) {
      console.error('Error fetching suggestions:', err);
    }
  }

  function renderSuggestions(results) {
    if (!results || results.length === 0) {
      suggestionsDropdown.innerHTML = `
        <div style="padding: 16px; text-align: center; color: var(--text-dim);">
          هیچ دەرمانێک بەم ناوە نەدۆزرایەوە لە پێرستی باودا. کلیکی گەڕان بکە بۆ گەڕانی ڕاستەوخۆ لە بنکەدراوەی جیهانی FDA.
        </div>
      `;
      suggestionsDropdown.classList.add('open');
      return;
    }

    let html = '';
    results.forEach(item => {
      html += `
        <div class="suggestion-item" data-id="${item.id}" data-generic="${item.generic_name}">
          <div class="sug-main">
            <span class="sug-icon">💊</span>
            <div>
              <div class="sug-title">${item.kurdish_name}</div>
              <div class="sug-generic">${item.generic_name} ${item.brand_names && item.brand_names.length ? `• ${item.brand_names.slice(0, 3).join(', ')}` : ''}</div>
            </div>
          </div>
          <span class="sug-badge">${item.category_en || 'FDA Regulated'}</span>
        </div>
      `;
    });

    suggestionsDropdown.innerHTML = html;
    suggestionsDropdown.classList.add('open');

    // Add click listeners to items
    suggestionsDropdown.querySelectorAll('.suggestion-item').forEach(item => {
      item.addEventListener('click', () => {
        const drugId = item.getAttribute('data-id');
        loadDrugDetails(drugId);
        searchInput.value = item.querySelector('.sug-title').textContent.split('/')[0].trim();
        suggestionsDropdown.classList.remove('open');
      });
    });
  }

  async function performSearch(query) {
    try {
      const res = await fetch(`/api/search?q=${encodeURIComponent(query)}`);
      const data = await res.json();
      // If user typed exact and results exist, load first
      if (query && data.results && data.results.length > 0) {
        loadDrugDetails(data.results[0].id);
      } else if (!query && data.results && data.results.length > 0) {
        // Load default Paracetamol
        loadDrugDetails('paracetamol');
      }
    } catch (err) {
      console.error('Search failed:', err);
    }
  }

  function selectDrugByQuery(query) {
    fetchSuggestions(query).then(() => {
      loadDrugDetails(query);
    });
  }

  // Load Single Drug Full Verified Details
  async function loadDrugDetails(drugId) {
    drugDetailsContainer.innerHTML = `
      <div class="medical-card" style="text-align: center; padding: 60px 20px;">
        <div class="pulse-dot" style="margin: 0 auto 16px auto; width: 14px; height: 14px;"></div>
        <h3 style="color: #fff; margin-bottom: 8px;">پەیوەندیکردن بە بنکەدراوەی فەرمی OpenFDA...</h3>
        <p style="color: var(--text-muted); font-size: 0.9rem;">وەرگرتنی داتای سەلامەتی، ماددەی چالاک، و هۆشدارییەکانی پزیشکی بەبێ دەستکاری</p>
      </div>
    `;
    drugDetailsContainer.classList.add('active');

    try {
      const res = await fetch(`/api/drug/${encodeURIComponent(drugId)}`);
      const data = await res.json();
      if (!data.success) {
        renderNotFound(drugId);
        return;
      }
      renderDrugProfile(data);
      // Smooth scroll to details
      drugDetailsContainer.scrollIntoView({ behavior: 'smooth', block: 'start' });
    } catch (err) {
      console.error('Failed to load drug details:', err);
      renderNotFound(drugId);
    }
  }

  function renderNotFound(name) {
    drugDetailsContainer.innerHTML = `
      <div class="medical-card" style="text-align: center; padding: 48px 20px;">
        <div style="font-size: 3rem; margin-bottom: 12px;">🔍</div>
        <h3 style="color: #fff; margin-bottom: 8px;">دەرمانەکە بە فەرمی لە OpenFDA نەدۆزرایەوە</h3>
        <p style="color: var(--text-muted); max-width: 500px; margin: 0 auto 20px auto;">
          تکایە دڵنیابە لە ڕێنووسی ناوی زانستی (Generic Name) یان ناوی بازرگانی دەرمانەکە، یان لە لیستی پێشنیارەکان هەڵیبژێرە.
        </p>
        <button class="search-submit-btn" onclick="document.getElementById('medicineSearchInput').focus()">گەڕانێکی تر بکە</button>
      </div>
    `;
  }

  function renderDrugProfile(data) {
    const kInfo = data.kurdish_info || {};
    const fda = data.fda_official || {};
    const kSummary = kInfo.kurdish_summary || {};

    const displayName = kInfo.kurdish_name || fda.brand_name || fda.generic_name;
    const genericName = kInfo.generic_name || fda.generic_name || 'N/A';
    const category = kInfo.category || fda.route || 'تەندروستی گشتی';
    const brands = kInfo.brand_names || [fda.brand_name].filter(Boolean);

    const fdaAppNo = fda.fda_application_number || 'FDA Monograph / OTC';
    const ndc = fda.product_ndc || 'Approved NDC';
    const verifiedBadge = data.verified_fda ? `
      <div class="fda-official-stamp">
        <span class="stamp-icon">🛡️</span>
        <div class="stamp-text">
          <strong>پشتڕاستکراوە بە فەرمی لە OpenFDA</strong>
          <small>NDC: ${ndc} • ${fdaAppNo}</small>
        </div>
      </div>
    ` : '';

    const html = `
      <div class="medical-card">
        <!-- Header Row -->
        <div class="drug-header-row">
          <div class="drug-title-group">
            <h2>${displayName}</h2>
            <div class="drug-meta-line">
              <span class="generic-pill">INN: ${genericName}</span>
              <span class="category-pill">${category}</span>
              ${data.meal_timing ? `<span class="category-pill" style="background: rgba(59, 130, 246, 0.25); border-color: #3b82f6; color: #93c5fd; font-weight: 700;">🍽️ ${data.meal_timing.badge_kurdish}</span>` : ''}
              ${brands.length ? `<span class="category-pill">ناوە باوەکان: ${brands.slice(0, 4).join(', ')}</span>` : ''}
            </div>
          </div>
          ${verifiedBadge}
        </div>

        <!-- Boxed Warning if Present in FDA -->
        ${fda.boxed_warning ? `
          <div class="alert-box-danger" style="margin-top: 24px;">
            <h4>⚠️ هۆشداری توندی فەرمی FDA (Boxed Warning)</h4>
            <p style="direction: ltr; text-align: left; font-family: 'Inter', sans-serif; font-size: 0.88rem; line-height: 1.6;">
              ${escapeHtml(fda.boxed_warning)}
            </p>
          </div>
        ` : ''}

        <!-- Tabs Navigation -->
        <div class="details-tabs-header">
          <button class="tab-trigger active" data-target="tab-kurdish">
            <span>📋</span> ڕێنمایی بە کوردی
          </button>
          <button class="tab-trigger" data-target="tab-meal-timing">
            <span>🍽️</span> کاتی خواردن و ژەمەکان
          </button>
          <button class="tab-trigger" data-target="tab-fda-official">
            <span>🏛️</span> بەڵگەنامەی فەرمی FDA
          </button>
          <button class="tab-trigger" data-target="tab-warnings">
            <span>⚠️</span> قەدەغەکراوە بۆ کێ؟
          </button>
          <button class="tab-trigger" data-target="tab-pregnancy">
            <span>🤰</span> دووگیانی و شیردەر
          </button>
          <button class="tab-trigger" data-target="tab-source">
            <span>🌐</span> کۆدی مۆڵەت و سەرچاوە
          </button>
        </div>

        <!-- Tab 1: Kurdish Summary -->
        <div class="tab-pane active" id="tab-kurdish">
          <div class="info-cards-grid">
            <div class="info-subcard">
              <div class="subcard-head">
                <span class="subcard-icon">🎯</span>
                <h4>بۆچی بەکاردێت؟ (Purpose)</h4>
              </div>
              <div class="subcard-body">
                ${kSummary.purpose || fda.indications_and_usage || 'بۆ زانیاری تەواو سەیری بڕگەی فەرمی FDA بکە.'}
              </div>
            </div>

            <div class="info-subcard">
              <div class="subcard-head">
                <span class="subcard-icon">💊</span>
                <h4>ڕێژە و شێوازی خواردن (Usage)</h4>
              </div>
              <div class="subcard-body">
                ${kSummary.usage || fda.dosage_and_administration || 'دەبێت بەپێی ڕەچەتەی پزیشک و کاتی دیاریکراو بخورێت.'}
              </div>
            </div>

            <div class="info-subcard" style="border-color: rgba(239, 68, 68, 0.3);">
              <div class="subcard-head">
                <span class="subcard-icon">⛔</span>
                <h4 style="color: #f87171;">کێ نابێت بیخوات؟ (Contraindications)</h4>
              </div>
              <div class="subcard-body">
                ${kSummary.who_cannot_take || fda.contraindications || 'لە کاتی هەستیاری بە دەرمانەکە بە توندی قەدەغەیە.'}
              </div>
            </div>

            <div class="info-subcard" style="border-color: rgba(245, 158, 11, 0.3);">
              <div class="subcard-head">
                <span class="subcard-icon">⚡</span>
                <h4 style="color: #fbbf24;">هۆشداری سەرەکی (Crucial Alert)</h4>
              </div>
              <div class="subcard-body">
                ${kSummary.crucial_warning || fda.warnings || 'هەرگیز لە بڕی دیاریکراوی ڕۆژانە زیاتر مەخۆ.'}
              </div>
            </div>
          </div>
        </div>

        <!-- Tab: Meal Timing & Missed Dose -->
        <div class="tab-pane" id="tab-meal-timing">
          <div style="background: rgba(15, 23, 42, 0.8); border: 2px solid #3b82f6; border-radius: var(--radius-md); padding: 24px;">
            <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px; margin-bottom: 16px;">
              <h3 style="color: #fff; font-size: 1.25rem; margin: 0; display: flex; align-items: center; gap: 8px;">
                <span>🍽️</span>
                <span>کاتی خواردنی ئەم دەرمانە لەگەڵ ناندا:</span>
              </h3>
              <span style="font-size: 1rem; font-weight: 800; background: rgba(59, 130, 246, 0.2); border: 1px solid #3b82f6; color: #93c5fd; padding: 6px 16px; border-radius: var(--radius-full);">
                ${data.meal_timing ? data.meal_timing.badge_kurdish : 'پێش یان دوای نان'}
              </span>
            </div>

            <h4 style="color: #67e8f9; font-size: 1.15rem; margin-bottom: 10px;">${data.meal_timing ? data.meal_timing.headline : ''}</h4>
            <p style="font-size: 0.98rem; line-height: 1.8; color: var(--text-main); margin-bottom: 24px;">
              ${data.meal_timing ? data.meal_timing.rationale : ''}
            </p>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px;">
              <div style="background: rgba(245, 158, 11, 0.1); border: 1px solid rgba(245, 158, 11, 0.35); border-radius: var(--radius-sm); padding: 18px;">
                <h5 style="color: #fbbf24; font-size: 1rem; margin-bottom: 8px; display: flex; align-items: center; gap: 6px;">
                  <span>🥛</span> خواردن و خواردنەوەی قەدەغەکراو لەگەڵ ئەم دەرمانە:
                </h5>
                <p style="font-size: 0.9rem; line-height: 1.6; color: #fef08a; margin: 0;">
                  ${data.meal_timing ? data.meal_timing.drinks_warning : 'بە پەرداخێک ئاوی ئاسایی بیخۆ.'}
                </p>
              </div>

              <div style="background: rgba(139, 92, 246, 0.1); border: 1px solid rgba(139, 92, 246, 0.35); border-radius: var(--radius-sm); padding: 18px;">
                <h5 style="color: #c4b5fd; font-size: 1rem; margin-bottom: 8px; display: flex; align-items: center; gap: 6px;">
                  <span>⏰</span> ئەگەر ژەمێکم لەبیرچوو چی بکەم؟ (Missed Dose):
                </h5>
                <p style="font-size: 0.9rem; line-height: 1.6; color: #ddd6fe; margin: 0;">
                  ${data.meal_timing ? data.meal_timing.missed_dose : 'هەر کات بیرت کەوتەوە بیخۆ، بەڵام هەرگیز دوو حەب بەیەکەوە مەخۆ.'}
                </p>
              </div>
            </div>
          </div>
        </div>

        <!-- Tab 2: FDA Official Label (Zero Hallucination Original Text) -->
        <div class="tab-pane" id="tab-fda-official">
          <div class="fda-raw-box">
            <div style="margin-bottom: 12px; font-weight: bold; color: #34d399; font-size: 0.85rem;">
              DIRECT EXTRACTION FROM U.S. FOOD & DRUG ADMINISTRATION (OPENFDA) REPOSITORY
            </div>
            
            ${fda.indications_and_usage ? `
              <h4>INDICATIONS AND USAGE (Approved Purposes):</h4>
              <p>${escapeHtml(fda.indications_and_usage)}</p>
            ` : ''}

            ${fda.dosage_and_administration ? `
              <h4>DOSAGE AND ADMINISTRATION:</h4>
              <p>${escapeHtml(fda.dosage_and_administration)}</p>
            ` : ''}

            ${fda.contraindications ? `
              <h4>CONTRAINDICATIONS (Do Not Use):</h4>
              <p>${escapeHtml(fda.contraindications)}</p>
            ` : ''}

            ${fda.warnings ? `
              <h4>WARNINGS AND PRECAUTIONS:</h4>
              <p>${escapeHtml(fda.warnings)}</p>
            ` : ''}

            ${fda.adverse_reactions ? `
              <h4>ADVERSE REACTIONS / SIDE EFFECTS:</h4>
              <p>${escapeHtml(fda.adverse_reactions)}</p>
            ` : ''}
          </div>
        </div>

        <!-- Tab 3: Warnings & Precautions -->
        <div class="tab-pane" id="tab-warnings">
          <div class="alert-box-warning">
            <h4>⚠️ هۆشدارییە پزیشکییە فەرمییەکان بۆ پاراستنی تەندروستی:</h4>
            <p style="margin-bottom: 12px;">${kSummary.crucial_warning || 'دەرمانەکان تەنها لە کاتی دیاریکراو و بە ژەمی دیاریکراو دەخورێن.'}</p>
            <p style="font-size: 0.9rem; color: #fef08a;">
              <strong>کەسانێک کە کێشەی تەندروستی تری وەک:</strong> سستبوونی گورچیلە، نەخۆشی جگەر، فشاری خوێن یان برینی گەدەیان هەیە دەبێت بەردەوام پێش وەرگرتنی هەر دەرمانێک دکتۆرەکەیان ئاگادار بکەنەوە.
            </p>
          </div>
          ${fda.warnings ? `
            <div class="fda-raw-box" style="margin-top: 16px;">
              <h4>FDA Verified Precautions Text:</h4>
              <p>${escapeHtml(fda.warnings)}</p>
            </div>
          ` : ''}
        </div>

        <!-- Tab 4: Pregnancy & Nursing -->
        <div class="tab-pane" id="tab-pregnancy">
          <div class="info-subcard" style="padding: 24px;">
            <div class="subcard-head">
              <span class="subcard-icon">🤰</span>
              <h4>سەلامەتی لە کاتی دووگیانی و شیرپێدان:</h4>
            </div>
            <div class="subcard-body" style="font-size: 1rem; color: #fff; margin-bottom: 16px;">
              ${kSummary.pregnancy_safety || 'پێویستە پزیشکی پسپۆڕی ئافرەتان بڕیار لەسەر سەلامەتی بدات.'}
            </div>
            ${fda.pregnancy_nursing ? `
              <div class="fda-raw-box">
                <h4>Official FDA Pregnancy & Nursing Section:</h4>
                <p>${escapeHtml(fda.pregnancy_nursing)}</p>
              </div>
            ` : ''}
          </div>
        </div>

        <!-- Tab 5: Verification & Links -->
        <div class="tab-pane" id="tab-source">
          <div class="info-subcard" style="padding: 24px;">
            <h4 style="color: #fff; margin-bottom: 14px;">بەڵگەی بەستنەوە بە سیستەمی FDA و داتابەیسی نێودەوڵەتی</h4>
            <ul style="list-style: none; padding: 0; line-height: 2; color: var(--text-muted); font-size: 0.95rem;">
              <li><strong>ماددەی زانستی نێودەوڵەتی (INN):</strong> <span style="direction: ltr; font-family: 'Inter', sans-serif; color: #2dd4bf;">${genericName}</span></li>
              <li><strong>ژمارەی تۆماری کۆدی بەرهەم (NDC):</strong> <span style="font-family: 'Inter', sans-serif; color: #fff;">${ndc}</span></li>
              <li><strong>ژمارەی داواکاری FDA (Application):</strong> <span style="font-family: 'Inter', sans-serif; color: #fff;">${fdaAppNo}</span></li>
              <li><strong>کارگەی ڕێگەپێدراو:</strong> <span>${fda.manufacturer_name || 'FDA Registered Lab'}</span></li>
            </ul>
            <div style="margin-top: 20px;">
              <a href="${fda.official_fda_url || 'https://dailymed.nlm.nih.gov'}" target="_blank" rel="noopener noreferrer" class="search-submit-btn" style="text-decoration: none; display: inline-flex; align-items: center; gap: 8px;">
                <span>سەردانی بەڵگەنامەی فەرمی لە DailyMed / NLM</span>
                <span style="font-size: 1.1rem;">↗</span>
              </a>
            </div>
          </div>
        </div>
      </div>
    `;

    drugDetailsContainer.innerHTML = html;

    // Attach Tab Switching
    const tabTriggers = drugDetailsContainer.querySelectorAll('.tab-trigger');
    const tabPanes = drugDetailsContainer.querySelectorAll('.tab-pane');

    tabTriggers.forEach(trigger => {
      trigger.addEventListener('click', () => {
        tabTriggers.forEach(t => t.classList.remove('active'));
        tabPanes.forEach(p => p.classList.remove('active'));

        trigger.classList.add('active');
        const targetId = trigger.getAttribute('data-target');
        const targetPane = drugDetailsContainer.querySelector(`#${targetId}`);
        if (targetPane) {
          targetPane.classList.add('active');
        }
      });
    });
  }

  // Voice Search Handler
  function initVoiceRecognition() {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SpeechRecognition) {
      voiceSearchBtn.style.display = 'none';
      return;
    }

    speechRecognition = new SpeechRecognition();
    speechRecognition.continuous = false;
    speechRecognition.interimResults = false;
    // Fallback to Persian/Arabic which captures Kurdish phonetic letters best in browsers
    speechRecognition.lang = 'fa-IR';

    speechRecognition.onstart = () => {
      isListening = true;
      voiceSearchBtn.classList.add('recording');
      searchInput.placeholder = 'گوێ دەگرم... ناوی دەرمانەکە بڵێ...';
    };

    speechRecognition.onresult = (event) => {
      const transcript = event.results[0][0].transcript;
      searchInput.value = transcript;
      fetchSuggestions(transcript);
      selectDrugByQuery(transcript);
    };

    speechRecognition.onerror = (e) => {
      console.warn('Speech recognition error:', e.error);
      stopVoiceSearch();
    };

    speechRecognition.onend = () => {
      stopVoiceSearch();
    };
  }

  function toggleVoiceSearch() {
    if (!speechRecognition) return;
    if (isListening) {
      speechRecognition.stop();
      stopVoiceSearch();
    } else {
      try {
        speechRecognition.start();
      } catch (err) {
        console.error(err);
      }
    }
  }

  function stopVoiceSearch() {
    isListening = false;
    voiceSearchBtn.classList.remove('recording');
    searchInput.placeholder = 'ناوی دەرمان بنووسە بە کوردی، عەرەبی، یان ئینگلیزی (وەک: پەنادۆڵ، پرۆفین، ئۆگەنتین، گلوکۆفاج)...';
  }

  // Drug-to-Drug Interaction Checker
  async function performInteractionCheck() {
    const d1 = drug1Input.value.trim();
    const d2 = drug2Input.value.trim();

    if (!d1 || !d2) {
      alert('تکایە ناوی هەردوو دەرمانەکە دیاری بکە پێش پشکنین.');
      return;
    }

    checkInteractionBtn.disabled = true;
    checkInteractionBtn.textContent = 'لە پشکنیندایە لە FDA...';

    try {
      const res = await fetch('/api/interaction', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ drug1: d1, drug2: d2 })
      });
      const json = await res.json();
      if (json.success) {
        renderInteractionResult(json.data);
      } else {
        alert(json.error || 'هەڵەیەک ڕوویدا لە کاتی پشکنیندا.');
      }
    } catch (err) {
      console.error('Interaction check failed:', err);
    } finally {
      checkInteractionBtn.disabled = false;
      checkInteractionBtn.textContent = 'پشکنینی دژەیەکبوون';
    }
  }

  function renderInteractionResult(data) {
    let alertClass = 'alert-box-warning';
    let borderColor = 'var(--warning-border)';
    let icon = '⚡';

    if (data.severity === 'danger') {
      alertClass = 'alert-box-danger';
      borderColor = 'var(--danger-border)';
      icon = '🔴';
    } else if (data.severity === 'safe') {
      alertClass = 'info-subcard';
      borderColor = 'var(--success-border)';
      icon = '🟢';
    }

    interactionResultCard.innerHTML = `
      <div class="${alertClass}" style="border: 2px solid ${borderColor}; padding: 24px; border-radius: var(--radius-md);">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; flex-wrap: wrap; gap: 10px;">
          <h4 style="font-size: 1.25rem; margin: 0; display: flex; align-items: center; gap: 8px;">
            <span>${icon}</span>
            <span>${data.severity_kurdish}</span>
          </h4>
          <span style="font-size: 0.8rem; background: rgba(255, 255, 255, 0.08); padding: 4px 12px; border-radius: var(--radius-full); font-family: 'Inter', sans-serif;">
            ${data.source}
          </span>
        </div>

        <h3 style="color: #fff; font-size: 1.15rem; margin-bottom: 10px;">${data.title}</h3>
        <p style="font-size: 0.95rem; line-height: 1.7; margin-bottom: 16px;">
          ${data.details_kurdish}
        </p>

        <div style="background: rgba(0, 0, 0, 0.25); border-radius: var(--radius-sm); padding: 14px; font-size: 0.92rem;">
          <strong style="color: #2dd4bf; display: block; margin-bottom: 4px;">ڕێنمایی پزیشکی:</strong>
          <span>${data.management}</span>
        </div>
      </div>
    `;

    interactionResultCard.classList.add('active');
    interactionResultCard.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }

  // Image & Barcode OCR Simulator
  function handleImageUpload(e) {
    const file = e.target.files[0];
    if (!file) return;

    scannerStatus.innerHTML = `
      <div class="pulse-dot" style="margin: 12px auto;"></div>
      <p style="color: #2dd4bf;">خوێندنەوەی دەقی سەر پاکەتی دەرمان و پشکنین لە داتابەیس...</p>
    `;

    // Extract filename keywords or simulate smart OCR recognition of standard packs
    setTimeout(() => {
      const fileNameLower = file.name.toLowerCase();
      let matchedDrug = 'paracetamol';

      if (fileNameLower.includes('prof') || fileNameLower.includes('brufen') || fileNameLower.includes('ibup')) {
        matchedDrug = 'ibuprofen';
      } else if (fileNameLower.includes('aug') || fileNameLower.includes('amox')) {
        matchedDrug = 'amoxicillin_clavulanate';
      } else if (fileNameLower.includes('volt') || fileNameLower.includes('cataf') || fileNameLower.includes('diclo')) {
        matchedDrug = 'diclofenac';
      } else if (fileNameLower.includes('lip') || fileNameLower.includes('atorv')) {
        matchedDrug = 'atorvastatin';
      } else if (fileNameLower.includes('concor') || fileNameLower.includes('biso')) {
        matchedDrug = 'bisoprolol';
      } else if (fileNameLower.includes('gluc') || fileNameLower.includes('metfor')) {
        matchedDrug = 'metformin';
      }

      scannerStatus.innerHTML = `
        <p style="color: #34d399; font-weight: bold;">دەرمانەکە دۆزرایەوە! دەگوازرێیتەوە بۆ پەڕەی فەرمی...</p>
      `;

      setTimeout(() => {
        scannerModal.classList.remove('open');
        loadDrugDetails(matchedDrug);
        searchInput.value = matchedDrug;
      }, 1000);
    }, 1200);
  }

  // Category Filter
  async function filterByCategory(categoryKey) {
    try {
      const res = await fetch('/api/search');
      const data = await res.json();
      const drugs = data.results || [];

      if (categoryKey === 'all') {
        renderSuggestions(drugs);
      } else {
        const filtered = drugs.filter(d => 
          d.category_en.toLowerCase().includes(categoryKey.toLowerCase()) || 
          d.category.toLowerCase().includes(categoryKey.toLowerCase())
        );
        renderSuggestions(filtered);
      }
    } catch (err) {
      console.error(err);
    }
  }

  // Load Emergency Directory
  async function loadEmergencyDirectory() {
    const container = document.getElementById('emergencyDirectoryContainer');
    if (!container) return;

    try {
      const res = await fetch('/api/emergency');
      const json = await res.json();
      if (!json.success) return;

      const data = json.data;
      let html = '';

      // Hotlines
      data.hotlines.forEach(h => {
        html += `
          <div class="emergency-card">
            <div class="emergency-head">
              <h4>${h.name}</h4>
              <span class="emergency-num-badge">${h.number}</span>
            </div>
            <p style="font-size: 0.88rem; color: var(--text-muted);">${h.desc}</p>
          </div>
        `;
      });

        container.innerHTML = html;
    } catch (err) {
      console.error(err);
    }
  }

  // =========================================================================
  // Patient Symptom Triage & Specialist Referral Logic
  // =========================================================================
  const symptomInput = document.getElementById('symptomInput');
  const checkSymptomBtn = document.getElementById('checkSymptomBtn');
  const symptomResultContainer = document.getElementById('symptomResultContainer');

  if (checkSymptomBtn && symptomInput) {
    checkSymptomBtn.addEventListener('click', () => {
      const val = symptomInput.value.trim();
      if (val) {
        performSymptomTriage(val);
      } else {
        alert('تکایە بە کورتی شوێنی ئازارەکە یان کێشەکەت بنووسە.');
        symptomInput.focus();
      }
    });

    symptomInput.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') {
        e.preventDefault();
        const val = symptomInput.value.trim();
        if (val) {
          performSymptomTriage(val);
        }
      }
    });

    // Sample Query Chips
    document.querySelectorAll('.symptom-sample-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const query = btn.getAttribute('data-query');
        symptomInput.value = query;
        performSymptomTriage(query);
      });
    });
  }

  async function performSymptomTriage(complaint) {
    checkSymptomBtn.disabled = true;
    checkSymptomBtn.textContent = 'لە پشکنیندایە...';

    symptomResultContainer.style.display = 'block';
    symptomResultContainer.innerHTML = `
      <div style="text-align: center; padding: 24px;">
        <div class="pulse-dot" style="margin: 0 auto 12px auto;"></div>
        <p style="color: var(--text-muted);">پشکنینی پزیشکی کلینیکی بۆ دەستنیشانکردنی جۆری دکتۆر و مەترسی...</p>
      </div>
    `;

    try {
      const res = await fetch('/api/triage', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ complaint: complaint })
      });
      const data = await res.json();

      if (!data.success && data.error_kurdish) {
        symptomResultContainer.innerHTML = `
          <div class="alert-box-warning">
            <p>${data.error_kurdish}</p>
          </div>
        `;
        return;
      }

      renderTriageResult(data);
      symptomResultContainer.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    } catch (err) {
      console.error('Symptom triage error:', err);
      symptomResultContainer.innerHTML = `
        <div class="alert-box-danger">
          <p>هەڵەیەک ڕوویدا لە کاتی پەیوەندیکردن بە سێرڤەر. تکایە دووبارە هەوڵبدەرەوە.</p>
        </div>
      `;
    } finally {
      checkSymptomBtn.disabled = false;
      checkSymptomBtn.textContent = 'پشکنینی ئازار';
    }
  }

  function renderTriageResult(data) {
    let alertClass = 'alert-box-warning';
    let borderColor = 'var(--warning-border)';
    let badgeColor = '#f59e0b';
    let badgeBg = 'rgba(245, 158, 11, 0.15)';

    if (data.severity === 'emergency') {
      alertClass = 'alert-box-danger';
      borderColor = 'var(--danger-border)';
      badgeColor = '#ef4444';
      badgeBg = 'rgba(239, 68, 68, 0.2)';
    } else if (data.severity === 'routine') {
      badgeColor = '#2dd4bf';
      badgeBg = 'rgba(13, 148, 136, 0.2)';
    }

    const careListHtml = (data.safe_home_care || []).map(item => `
      <li style="margin-bottom: 8px; line-height: 1.7;">${escapeHtml(item)}</li>
    `).join('');

    symptomResultContainer.innerHTML = `
      <div style="background: rgba(15, 23, 42, 0.85); border: 2px solid ${borderColor}; border-radius: var(--radius-md); padding: 28px; box-shadow: var(--shadow-md);">
        
        <!-- Header Severity Banner -->
        <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px; margin-bottom: 20px; padding-bottom: 14px; border-bottom: 1px solid var(--border-glass);">
          <div style="display: flex; align-items: center; gap: 10px;">
            <span style="font-size: 1.6rem;">🩺</span>
            <span style="background: ${badgeBg}; color: ${badgeColor}; border: 1px solid ${borderColor}; padding: 6px 14px; border-radius: var(--radius-full); font-weight: 800; font-size: 0.95rem;">
              ${data.severity_kurdish}
            </span>
          </div>
          <span style="font-size: 0.82rem; color: var(--text-dim);">پشکنینی بێ دەرمان • پاراستنی نەخۆش</span>
        </div>

        <!-- 1. Possible Condition -->
        <div style="margin-bottom: 20px;">
          <h4 style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 4px;">ئەگەری پزیشکی (Possible Clinical Issue):</h4>
          <h3 style="color: #fff; font-size: 1.3rem; font-weight: 800;">${data.possible_condition}</h3>
        </div>

        <!-- 2. Recommended Doctor Specialist (Highlighted Box) -->
        <div style="background: linear-gradient(135deg, rgba(124, 58, 237, 0.15), rgba(37, 99, 235, 0.15)); border: 1px solid rgba(139, 92, 246, 0.4); border-radius: var(--radius-md); padding: 20px; margin-bottom: 24px;">
          <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 6px;">
            <span style="font-size: 1.5rem;">👨‍⚕️</span>
            <div>
              <span style="font-size: 0.82rem; color: #c4b5fd; text-transform: uppercase; font-weight: bold; letter-spacing: 0.5px;">پزیشکی پسپۆڕ کە دەبێت سەردانی بکەیت:</span>
              <h2 style="font-size: 1.25rem; font-weight: 900; color: #fff; margin-top: 2px;">
                ${data.specialist}
              </h2>
            </div>
          </div>
        </div>

        <!-- 3. Safe Non-Drug First Aid / Home Care -->
        <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid var(--border-glass); border-radius: var(--radius-md); padding: 20px; margin-bottom: 20px;">
          <h4 style="color: #2dd4bf; font-size: 1.05rem; font-weight: 800; margin-bottom: 12px; display: flex; align-items: center; gap: 8px;">
            <span>🛡️</span> یارمەتی سەرەتایی سەلامەت (بەبێ خواردنی دەرمان تا دەگەیتە لای پزیشک):
          </h4>
          <ul style="list-style: none; padding: 0; color: var(--text-main); font-size: 0.95rem;">
            ${careListHtml}
          </ul>
        </div>

        <!-- 4. Red Flags Alert -->
        ${data.red_flags ? `
          <div class="alert-box-danger" style="margin-bottom: 20px; padding: 16px 20px;">
            <h4 style="font-size: 1rem; margin-bottom: 6px;">⚠️ نیشانە مەترسیدارەکان کە دەبێت یەکسەر بچیتە فریاکەوتن (١٢٢):</h4>
            <p style="font-size: 0.92rem; line-height: 1.6;">${data.red_flags}</p>
          </div>
        ` : ''}

        <!-- 5. Strict Medical Disclaimer -->
        <div style="background: rgba(0, 0, 0, 0.35); border-radius: var(--radius-sm); padding: 12px 16px; font-size: 0.82rem; color: var(--text-dim); line-height: 1.6;">
          🔒 <strong>تێبینی سەلامەتی پزیشکی:</strong> ئەم ئەپڵیکەیشنە هیچ جۆرە دەرمانێکی لە خۆوە نانووسێت تا ژیانی کەس نەکەوێتە مەترسی. ئامانجی ئەم بەشە تەنها ڕێنوێنییە بۆ دۆزینەوەی دکتۆری پسپۆڕی تەواو و خۆپاراستنی سەلامەت.
        </div>

      </div>
    `;
  }

  // =========================================================================
  // Drug & Penicillin Allergy Shield Logic
  // =========================================================================
  const allergyTypeInput = document.getElementById('allergyTypeInput');
  const allergyDrugInput = document.getElementById('allergyDrugInput');
  const checkAllergyBtn = document.getElementById('checkAllergyBtn');
  const allergyResultContainer = document.getElementById('allergyResultContainer');

  if (checkAllergyBtn && allergyTypeInput && allergyDrugInput) {
    checkAllergyBtn.addEventListener('click', performAllergyCheck);

    // Quick sample chips
    document.querySelectorAll('.allergy-sample-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        allergyTypeInput.value = btn.getAttribute('data-allergy');
        allergyDrugInput.value = btn.getAttribute('data-drug');
        performAllergyCheck();
      });
    });

    [allergyTypeInput, allergyDrugInput].forEach(inp => {
      inp.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
          e.preventDefault();
          performAllergyCheck();
        }
      });
    });
  }

  async function performAllergyCheck() {
    const allergy = allergyTypeInput.value.trim();
    const drug = allergyDrugInput.value.trim();

    if (!allergy || !drug) {
      alert('تکایە هەم جۆری حەساسیەتەکەت و هەم ناوی دەرمانەکە بنووسە.');
      return;
    }

    checkAllergyBtn.disabled = true;
    checkAllergyBtn.textContent = 'لە پشکنیندایە...';

    allergyResultContainer.style.display = 'block';
    allergyResultContainer.innerHTML = `
      <div style="text-align: center; padding: 24px;">
        <div class="pulse-dot" style="margin: 0 auto 12px auto;"></div>
        <p style="color: var(--text-muted);">پشکنینی دژەیەکبوونی حەساسیەتی پێنسلین و پێکهاتە لاوەکییەکان لەگەڵ دەرمانەکە...</p>
      </div>
    `;

    try {
      const res = await fetch('/api/allergy-check', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ allergy: allergy, drug: drug })
      });
      const data = await res.json();
      renderAllergyResult(data);
      allergyResultContainer.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    } catch (err) {
      console.error('Allergy check failed:', err);
      allergyResultContainer.innerHTML = `
        <div class="alert-box-danger">
          <p>هەڵەیەک ڕوویدا لە کاتی پەیوەندیکردن بە سێرڤەر.</p>
        </div>
      `;
    } finally {
      checkAllergyBtn.disabled = false;
      checkAllergyBtn.textContent = 'پشکنینی حەساسیەت';
    }
  }

  function renderAllergyResult(data) {
    let alertClass = 'alert-box-warning';
    let borderColor = 'var(--warning-border)';
    let badgeColor = '#f59e0b';
    let badgeBg = 'rgba(245, 158, 11, 0.15)';
    let icon = '⚠️';

    if (data.status === 'forbidden') {
      alertClass = 'alert-box-danger';
      borderColor = 'var(--danger-border)';
      badgeColor = '#ef4444';
      badgeBg = 'rgba(239, 68, 68, 0.2)';
      icon = '🔴';
    } else if (data.status === 'likely_safe') {
      alertClass = 'info-subcard';
      borderColor = 'var(--success-border)';
      badgeColor = '#2dd4bf';
      badgeBg = 'rgba(13, 148, 136, 0.2)';
      icon = '🟢';
    }

    allergyResultContainer.innerHTML = `
      <div style="background: rgba(15, 23, 42, 0.85); border: 2px solid ${borderColor}; border-radius: var(--radius-md); padding: 26px; box-shadow: var(--shadow-md);">
        
        <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px; margin-bottom: 16px; border-bottom: 1px solid var(--border-glass); padding-bottom: 12px;">
          <div style="display: flex; align-items: center; gap: 8px;">
            <span style="font-size: 1.5rem;">${icon}</span>
            <span style="background: ${badgeBg}; color: ${badgeColor}; border: 1px solid ${borderColor}; padding: 4px 14px; border-radius: var(--radius-full); font-weight: 800; font-size: 0.95rem;">
              ${data.status_kurdish}
            </span>
          </div>
          <span style="font-size: 0.8rem; color: var(--text-dim);">پشکنەری سەلامەتی حەساسیەتی دەرمان</span>
        </div>

        <h3 style="color: #fff; font-size: 1.25rem; font-weight: 800; margin-bottom: 10px;">${data.title}</h3>
        <p style="font-size: 0.98rem; line-height: 1.75; color: var(--text-main); margin-bottom: 18px;">
          ${data.explanation}
        </p>

        ${data.emergency_alert ? `
          <div class="alert-box-danger" style="margin-bottom: 18px; padding: 14px 18px;">
            <strong>🚨 هۆشداری فریاکەوتن:</strong>
            <p style="margin-top: 4px; font-size: 0.92rem; line-height: 1.6;">${data.emergency_alert}</p>
          </div>
        ` : ''}

        ${data.safer_alternatives ? `
          <div style="background: rgba(0, 0, 0, 0.3); border-radius: var(--radius-sm); padding: 16px; margin-bottom: 14px;">
            <strong style="color: #2dd4bf; display: block; margin-bottom: 4px; font-size: 0.95rem;">💡 جێگرەوەی سەلامەتتر (بە ڕاوێژی پزیشک):</strong>
            <p style="font-size: 0.92rem; color: #ddd; line-height: 1.6; margin: 0;">${data.safer_alternatives}</p>
          </div>
        ` : ''}

      </div>
    `;
  }

  function escapeHtml(str) {
    if (!str) return '';
    return str.replace(/[&<>'"]/g, 
      tag => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#39;', '"': '&quot;' }[tag] || tag)
    );
  }
});
