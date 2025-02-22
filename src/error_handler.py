import os
from datetime import datetime

LOG_FILES = {
    "General": "error_logs/errors.log",
    "API": "error_logs/api_errors.log",
    "Git": "error_logs/git_errors.log"
}

def log_error(error_type, message):
    """
    Logs errors into the appropriate log file with a timestamp.
    """
    log_file = LOG_FILES.get(error_type, LOG_FILES["General"])
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    log_entry = f"[{timestamp}] [{error_type}] {message}\n"
    
    try:
        os.makedirs("error_logs", exist_ok=True)  # Ensure the log directory exists
        with open(log_file, "a") as file:
            file.write(log_entry)
    except Exception as e:
        print(f"⚠️ Failed to write to log file: {str(e)}")
