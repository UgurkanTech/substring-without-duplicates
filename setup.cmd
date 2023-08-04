::Author: -Uğurkan Hoşgör
@echo off
for /F %%a in ('echo prompt $E ^| cmd') do set "ESC=%%a"
copy /y ".\question.py" ".\question_c.pyx"
python setup.py build_ext --inplace
echo ^%ESC%[33mWaiting 5 seconds..%ESC%[0m
timeout /t 5 /nobreak > NUL