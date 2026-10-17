@echo off
rem Double-click to collect the latest 3 days of arXiv cs.CV papers.
rem Output: result\<run date>\arxiv_csCV_<start>_to_<end>.csv, .xlsx and .html
rem Options are passed through, e.g.:
rem   run_collect_arxiv_cv.bat --start 2026-10-14 --end 2026-10-16
setlocal
cd /d "%~dp0"
chcp 65001 >nul
set PYTHONIOENCODING=utf-8

where python >nul 2>nul
if errorlevel 1 (
    echo Python was not found. Install Python 3.9 or newer and add it to PATH.
    goto end
)

python -c "import openpyxl" >nul 2>nul
if errorlevel 1 (
    echo Installing required packages...
    python -m pip install -r requirements.txt
    if errorlevel 1 goto end
)

echo Collecting arXiv cs.CV papers. This takes about 20 minutes...
python collect_arxiv_cv.py %*
if errorlevel 1 (
    echo.
    echo Failed. See the messages above.
    goto end
)
echo.
echo Done. Saved to the result folder.

:end
echo.
pause
