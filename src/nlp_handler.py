import requests
import os
import json
import re
from src.error_handler import log_error
from src.config import GEMINI_API_KEY, GEMINI_API_URL, API_TIMEOUT

def interpret_command(user_input):
    """
    Sends a natural language prompt to Gemini API and extracts only the Git command.
    """
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [{"parts": [{"text": f"Convert this into a single Git command without explanation: {user_input}"}]}]
    }
    url = f"{GEMINI_API_URL}?key={GEMINI_API_KEY}"

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=API_TIMEOUT)
        response.raise_for_status()
        result = response.json()

        # 🔍 Debugging: Print the full API response
        # print("\n🔍 API Raw Response:", json.dumps(result, indent=2))

        if "candidates" in result and result["candidates"]:
            full_response = result["candidates"][0]["content"]["parts"][0]["text"].strip()

            # ✅ Remove backticks (if present)
            full_response = full_response.strip("`")

            # ✅ Extract command from Markdown code blocks
            match = re.search(r"```(?:bash)?\n(.*?)\n```", full_response, re.DOTALL)
            git_command = match.group(1).strip() if match else full_response

            # ✅ Ensure the extracted text starts with "git"
            if git_command.startswith("git"):
                return git_command
            else:
                log_error("API", f"Invalid response: {full_response}")
                return "⚠️ Error: Unable to extract Git command."

        else:
            log_error("API", f"Invalid response format: {result}")
            return "⚠️ Error: Unable to process command."

    except requests.exceptions.Timeout:
        log_error("API", "Request timed out")
        return "⚠️ Error: API request timed out."

    except requests.exceptions.RequestException as e:
        log_error("API", f"Request failed: {str(e)}")
        return f"⚠️ Error: API request failed."
