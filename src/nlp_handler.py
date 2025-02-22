import requests
import json
import re
from src.error_handler import log_error
from src.config import GEMINI_API_KEY, GEMINI_API_URL, API_TIMEOUT

def interpret_command(user_input):
    """
    Sends a natural language prompt to Gemini API and extracts Git commands correctly.
    """
    headers = {"Content-Type": "application/json"}

    # 🔹 Check if the user input suggests multiple actions
    if any(keyword in user_input.lower() for keyword in ["and", ",", "then", "also"]):
        prompt = (f"Convert this into one or more Git commands without explanation. "
                  f"Only return the exact Git commands, separated by '&&' if needed: {user_input}")
    else:
        prompt = (f"Convert this into a single Git command without explanation. "
                  f"DO NOT combine multiple commands using '&&' or ';'. Only return the exact Git command: {user_input}")

    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    url = f"{GEMINI_API_URL}?key={GEMINI_API_KEY}"

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=API_TIMEOUT)
        response.raise_for_status()
        result = response.json()

        # Debugging: Print API response
        print("\n🔍 API Raw Response:", json.dumps(result, indent=2))

        if "candidates" in result and result["candidates"]:
            full_response = result["candidates"][0]["content"]["parts"][0]["text"].strip()

            # ✅ Remove Markdown formatting if present
            git_command = re.sub(r"```(?:bash)?\n(.*?)\n```", r"\1", full_response, flags=re.DOTALL).strip()

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
