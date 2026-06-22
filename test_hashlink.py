# test_hashlink.py
"""
Tests for HashLink module.
"""

import unittest
from hashlink import HashLink

class TestHashLink(unittest.TestCase):
    """Test cases for HashLink class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HashLink()
        self.assertIsInstance(instance, HashLink)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HashLink()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
