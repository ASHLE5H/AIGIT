#!/usr/bin/env python3

import sys
from src.nlp_handler import interpret_command
from src.git_wrapper import execute_git_command
from src.error_handler import log_error

def main():
    if len(sys.argv) < 2:
        print("Usage: aigit \"your command\"")
        sys.exit(1)

    user_input = sys.argv[1]
    git_command = interpret_command(user_input)

    if "Error" in git_command:
        log_error("General", f"Failed to interpret: {user_input}")
        print("⚠️ Error: Could not understand the command.")
        sys.exit(1)

    print(f"\n🔹 Translated Command: {git_command}\n")

    execute_response = input("Do you want to execute this command? (yes/no): ")
    if execute_response.lower() == "yes":
        output = execute_git_command(git_command)
        print(output)

if __name__ == "__main__":
    main()
