import unittest
from src.git_wrapper import execute_git_command

class TestGitWrapper(unittest.TestCase):
    def test_valid_git_command(self):
        """Test if a valid Git command executes successfully."""
        response = execute_git_command("git --version")
        self.assertIn("git version", response.lower())

    def test_invalid_git_command(self):
        """Test if an invalid Git command returns an error message."""
        response = execute_git_command("git invalidcommand")
        self.assertIn("Git Error", response)

    def test_unsafe_git_command(self):
        """Test if an unsafe command is blocked."""
        response = execute_git_command("rm -rf .git")
        self.assertIn("Error", response)

if __name__ == "__main__":
    unittest.main()
