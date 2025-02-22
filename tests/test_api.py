import unittest
from src.nlp_handler import interpret_command

class TestAPI(unittest.TestCase):
    def test_valid_command(self):
        """Test if a valid natural language input returns a Git command."""
        response = interpret_command("initialize the repository")
        self.assertIsInstance(response, str)
        self.assertTrue(response.startswith("git"))

    def test_invalid_command(self):
        """Test if an invalid input returns an error message."""
        response = interpret_command("do something random")
        self.assertIn("Error", response)

    def test_api_timeout(self):
        """Test API timeout handling."""
        global API_TIMEOUT
        API_TIMEOUT = 0.001  # Force timeout
        response = interpret_command("commit changes")
        self.assertIn("Error", response)

if __name__ == "__main__":
    unittest.main()
