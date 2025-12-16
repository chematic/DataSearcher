@echo off
REM Modules Installer

color 1F
title BETA INSTALL METHOD FOR PYTHON
cls

echo # CHECKING...
timeout /t 1 /nobreak > nul

where python > nul 2>&1
if %errorlevel% neq 0 (
    goto PNF
)

echo.
echo FOUND! Installing modules...
echo.

set M=pystyle requests

:L
if "%M%"=="" goto S

for /f "tokens=1*" %%A in ("%M%") do (
    set A=%%A
    set M=%%B
    
    echo Installing %%A...
    
    python -m pip install %%A 
    
    if %errorlevel% neq 0 (
        echo [FAIL] Error installing %%A. Network issue?
        goto IF
    ) else (
        echo [OK] %%A installed.
    )
    goto L
)


:S
echo.
echo # INSTALL COMPLETE
echo.
echo [OK] All dependencies installed. Ready to run.
timeout /t 5 > nul
goto E


:PNF
REM Python Logic Installation: BETA.
echo.
echo [FAIL] Python not found. Starting automatic installation (approx 2-3 mins)...
echo.
echo Please wait. Do NOT close the installer window.
timeout /t 3 > nul

set PYTHON_VERSION=3.10.11
set URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe
set INSTALLER_NAME=p.exe
set INSTALL_LOG=p_install.log

echo Downloading Python %PYTHON_VERSION%...
powershell -Command "(New-Object System.Net.WebClient).DownloadFile('%URL%', '%INSTALLER_NAME%')"

if exist %INSTALLER_NAME% (
    echo.
    echo Starting silent installation...
    
    %INSTALLER_NAME% /quiet InstallAllUsers=1 PrependPath=1 >> %INSTALL_LOG% 2>&1
 
    timeout /t 15 > nul 
    
    echo.
    echo Installation finished. Deleting temporary files...
    del %INSTALLER_NAME%
    del %INSTALL_LOG%
    
    echo.
    echo [RESTART] Rerunning installer to find Python and install modules...
    timeout /t 3 > nul
    
    start "" "%~dpnx0"
    exit /b 0

) else (
    echo.
    echo [CRITICAL FAIL] Failed to download Python. Check network connection.
    echo Cannot proceed without Python.
    echo.
    pause
    exit /b 1
)


:IF
echo.
echo [FAIL] Installation failed. Cannot proceed.
echo.
pause
exit /b 1


:E
title  
python main.py
exit /b 0