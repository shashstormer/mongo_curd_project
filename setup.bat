@echo off
setlocal
set NLM=^


set NL=^^^%NLM%%NLM%^%NLM%%NLM%

echo This Project has been devloped by shashstorm %NL%If any error occurs please ensure you have the following installed and updated %NL%1. Node%NL%2. Python 3.9 or above%NL%3. Sass (whichever version you prefer but it is suggested that you install dart sass using choco package manager)

REM Check if Python is installed
python --version 2>NUL
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python and try again.
)

REM Check if pip is installed
pip --version 2>NUL
if %errorlevel% neq 0 (
    echo pip is not installed. Please install pip and try again.
)

REM Install Python dependencies from requirements.txt
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo An error occurred while installing Python dependencies.
)

REM Check if Node.js is installed
node --version 2>NUL
if %errorlevel% neq 0 (
    echo Node.js is not installed. Please install Node.js and try again.
)

REM Check if npm is installed
npm --version 2>NUL
REM if %errorlevel% neq 0 (
    REM echo npm is not installed. Please install npm and try again.
REM )

REM Install Node.js dependencies (Tailwind CSS, Sass, etc.)
npm install
REM if %errorlevel% neq 0 (
    REM echo An error occurred while installing Node.js dependencies.
REM )
REM Display completion message
echo Setup is complete.
pause