import re

def sanitize_command(command):
    """
    Sanitizes the Git command to prevent dangerous operations.
    """
    dangerous_commands = ["rm -rf", "reset --hard", "rebase", "checkout", "push --force"]
    
    for dangerous in dangerous_commands:
        if dangerous in command:
            return "⚠️ Error: Unsafe command detected."
    
    return command

def format_output(output):
    """
    Formats command output for better readability.
    """
    return "\n".join(line.strip() for line in output.splitlines() if line.strip())

def is_valid_git_command(command):
    """
    Checks if the given string is a valid Git command format.
    """
    return re.match(r"^git\s+[a-zA-Z0-9\-_.]+", command) is not None
