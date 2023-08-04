::Author: -Uğurkan Hoşgör
@echo off
for /F %%a in ('echo prompt $E ^| cmd') do set "ESC=%%a"
python -m unittest -v test.py
echo ^%ESC%[33mWaiting 5 seconds..%ESC%[0m
timeout /t 5 /nobreak > NUL