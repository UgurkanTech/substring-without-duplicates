::Author: -Uğurkan Hoşgör
@echo off
for /F %%a in ('echo prompt $E ^| cmd') do set "ESC=%%a"
cls
echo ^%ESC%[32mClearing the project.%ESC%[0m
call ./clear.cmd
echo.
echo ^%ESC%[32mBuilding the project.%ESC%[0m
call ./setup.cmd
echo.
echo ^%ESC%[32mBenchmarking the project.%ESC%[0m
call ./benchmark.cmd
echo.
echo ^%ESC%[32mTesting the project.%ESC%[0m
call ./test.cmd
echo %ESC%[32m^<^<--DONE--^>^>.%ESC%[0m
pause