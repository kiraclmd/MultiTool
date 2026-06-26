@echo off
set "DEST=%USERPROFILE%\Desktop\Tool"

if exist "%DEST%" (
    echo File already here
) else (
    move "%~dp0Tool" "%DEST%" >nul 2>&1
    echo File moov
)
pause