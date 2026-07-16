@echo off
setlocal EnableDelayedExpansion

cd /d "%~dp0"

for %%f in (*.zip) do (
    set "name=%%~nf"

    rem If the filename ends with (1), remove it
    if "!name:~-3!"=="(1)" (
        set "out=!name:~0,-3!"
    ) else (
        set "out=!name!"
    )

    echo Extracting "%%f" to "!out!"
    "C:\Program Files\7-Zip\7z.exe" x "%%f" -o"." -y
)

pause