::Author: -Uğurkan Hoşgör
@echo off
for /F %%a in ('echo prompt $E ^| cmd') do set "ESC=%%a"
echo Benchmarking interpreted python code:
python -m timeit -n 300000 -s "from question import execute" "execute('ABBCDDEFGHII')"
echo.
echo Benchmarking Compiled CPython code:
python -m timeit -n 300000 -s "from question_c import execute" "execute('ABBCDDEFGHII')"
echo ^%ESC%[33mWaiting 5 seconds..%ESC%[0m
timeout /t 5 /nobreak > NUL