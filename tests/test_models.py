# tests/test_models.py

import unittest
from app import app, db
from app.models import Item

class TestModels(unittest.TestCase):
    def setUp(self):
        """Create a test client and a new database before each test."""
        self.app = app
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        """Clean up after each test."""
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_item_creation(self):
        """Test that an Item can be created."""
        with self.app.app_context():
            item = Item(name='Test Item', quantity=10)
            db.session.add(item)
            db.session.commit()
            self.assertEqual(item.name, 'Test Item')
            self.assertEqual(item.quantity, 10)

if __name__ == '__main__':
    unittest.main()
