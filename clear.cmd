::Author: -Uğurkan Hoşgör
@echo off
for /F %%a in ('echo prompt $E ^| cmd') do set "ESC=%%a"
del ".\question_c.c" 2>NUL
del ".\question_c.html" 2>NUL
del ".\question_c.pyx" 2>NUL
del ".\question_c.cp310-win_amd64.pyd" 2>NUL

rmdir /s /q ".\build" 2>NUL
rmdir /s /q ".\__pycache__" 2>NUL

echo Project is cleared.
echo ^%ESC%[33mWaiting 5 seconds..%ESC%[0m
