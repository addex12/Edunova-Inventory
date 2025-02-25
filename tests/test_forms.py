# tests/test_forms.py

import unittest
from app import app
from app.forms import ItemForm

class TestForms(unittest.TestCase):
    
    def setUp(self):
        """Set up a Flask test client before each test."""
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_item_form_validation(self):
        """Test that the form validation works correctly."""
        with self.app.app_context():  # Add this line
            form = ItemForm(name='Test Item', quantity=10)
            self.assertTrue(form.validate())  # Validate successfully

            form = ItemForm(name='', quantity=0)
            self.assertFalse(form.validate())  # Should fail validation

if __name__ == '__main__':
    unittest.main()
