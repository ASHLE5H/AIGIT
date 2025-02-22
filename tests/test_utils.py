import unittest
from src.utils import sanitize_command, format_output, is_valid_git_command

class TestUtils(unittest.TestCase):
    def test_sanitize_safe_command(self):
        """Test if a safe Git command passes through unchanged."""
        command = "git commit -m 'Initial commit'"
        self.assertEqual(sanitize_command(command), command)

    def test_sanitize_unsafe_command(self):
        """Test if an unsafe Git command is blocked."""
        command = "git reset --hard"
        self.assertIn("Error", sanitize_command(command))

    def test_format_output(self):
        """Test if output formatting removes unnecessary whitespace."""
        output = "  Line 1  \n\n  Line 2  \n"
        expected = "Line 1\nLine 2"
        self.assertEqual(format_output(output), expected)

    def test_valid_git_command(self):
        """Test if valid Git commands are correctly recognized."""
        self.assertTrue(is_valid_git_command("git add ."))
        self.assertTrue(is_valid_git_command("git push origin main"))

    def test_invalid_git_command(self):
        """Test if invalid commands are rejected."""
        self.assertFalse(is_valid_git_command("rm -rf /"))
        self.assertFalse(is_valid_git_command("echo 'Hello'"))

if __name__ == "__main__":
    unittest.main()
