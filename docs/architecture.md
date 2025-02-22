
---

#### **`architecture.md`** (High-Level Architecture Overview)  
```md
# AIGIT - Architecture Overview

## Overview
AIGIT is an AI-powered tool that translates natural language into Git commands, enabling seamless Git interactions through plain English.

## Components
### 1. **Natural Language Processing (NLP)**
- Uses DeepSeek API to interpret user input and map it to Git commands.

### 2. **Git Command Execution**
- Executes Git commands securely using `subprocess` in Python.
- Commands are sanitized before execution to prevent unsafe operations.

### 3. **Error Handling & Logging**
- Errors are logged in `error_logs/`.
- Separate logs for API issues, Git failures, and general errors.

### 4. **Packaging & Distribution**
- Built with PyInstaller (`aigit.exe`).
- Installer created using Inno Setup (`aigit.iss`).

## Workflow
1. **User Input**  
   - Example: `"initialize the repository"`
2. **NLP Processing**  
   - Converts input into `"git init"`
3. **Command Validation & Execution**  
   - Checks against `allowed_commands.txt`
   - Runs command safely in Git Bash
4. **Output & Logging**  
   - Displays results
   - Logs errors if needed

## System Requirements
- Windows 10/11
- Git installed & added to PATH
