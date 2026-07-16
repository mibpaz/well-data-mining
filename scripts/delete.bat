@echo off
cd /d "%~dp0"

for %%e in (
    tif
    cgm
    asc
    pdf
    pds
) do (
    del /s /q "*.%%e" 2>nul
)

pause