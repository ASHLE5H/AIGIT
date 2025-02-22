import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# DeepSeek API Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
API_TIMEOUT = 10  # Default timeout: 5 seconds

# Logging Configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Execution Settings
ALLOW_UNSAFE_COMMANDS = os.getenv("ALLOW_UNSAFE_COMMANDS", "False").lower() == "true"

# Rate Limits
MAX_REQUESTS_PER_MINUTE = int(os.getenv("MAX_REQUESTS_PER_MINUTE", 60))
