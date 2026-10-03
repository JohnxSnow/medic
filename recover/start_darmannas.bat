@echo off
title DarmanNas - Kurdish Official Medicine & FDA Verification System
chcp 65001 > nul
echo ==============================================================
echo       دەرمانناس - سیستەمی فەرمی زانیاری دەرمان بە بەستنەوەی FDA
echo                  DarmanNas Medicine Verification System
echo ==============================================================
echo.
echo سێرڤەر دەستپێدەکات...
echo سەردانی ئەم بەستەرە بکە لە وێبگەڕەکەت: http://127.0.0.1:5000
echo.

start "" "http://127.0.0.1:5000"
python app.py
pause
