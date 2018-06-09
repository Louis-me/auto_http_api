@ECHO OFF
start /wait pict33.msi /qn
set PICT_PATH=C:\Program Files (x86)\PICT
set ENV_PATH=%PATH%;%PICT_PATH%
taskkill /im explorer.exe /f
pause
start explorer.exe
@ECHO ON