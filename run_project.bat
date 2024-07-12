@echo off
rem Ensure Python is in the PATH, otherwise set the path to the Python executable
set PYTHON_PATH=python

rem Change directory to the Internship-Main directory
cd "%~dp0\Internship-Main"

rem Run the Python scripts
%PYTHON_PATH% home.py

rem Pause to keep the command window open
pause
