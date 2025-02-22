import subprocess
from src.error_handler import log_error

def execute_git_command(command):
    """
    Executes a Git command in the Git Bash environment and returns the output.
    """
    try:
        # ✅ Ensure there are staged changes before committing
        if "commit" in command:
            check_status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True, shell=True)
            if not check_status.stdout.strip():
                return "⚠️ Git Error: No changes to commit."

        # ✅ Execute the Git command
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        if result.returncode == 0:
            return result.stdout.strip() if result.stdout else "✅ Command executed successfully."
        else:
            error_msg = result.stderr.strip()

            # 🔍 Detect "fetch first" error and suggest `git pull --rebase`
            if "fetch first" in error_msg:
                return ("⚠️ Git Error: Your local branch is behind the remote.\n"
                        "💡 Fix: Run the following commands:\n"
                        "   git pull --rebase origin main\n"
                        "   git push origin main")

            # 🔍 Detect authentication failure
            if "authentication failed" in error_msg.lower():
                return "⚠️ Git Error: Authentication failed. Make sure you are logged in using `git credential fill` or set up SSH keys."

            log_error("Git", f"Failed command: {command}\nError: {error_msg}")
            return f"⚠️ Git Error: {error_msg}"

    except Exception as e:
        log_error("Git", f"Exception while executing '{command}': {str(e)}")
        return f"⚠️ Error: Failed to execute Git command."
