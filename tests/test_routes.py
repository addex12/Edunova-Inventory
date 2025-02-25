# tests/test_routes.py

import unittest
from app import app, db
from app.models import Item

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()
            # Add test data here:
            item = Item(name='Test Item', quantity=10)
            db.session.add(item)
            db.session.commit()

    def tearDown(self):
        """Clean up after each test."""
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_index_route(self):
        """Test the index route."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Item', response.data)

    def test_add_item_route(self):
        """Test the add item route."""
        response = self.client.post('/add', data={'name': 'New Item', 'quantity': 15})
        with self.app.app_context():
            item = Item.query.filter_by(name='New Item').first()
            self.assertIsNotNone(item)
            self.assertEqual(item.quantity, 15)
        self.assertEqual(response.status_code, 302)  # Check for redirection

if __name__ == '__main__':
    unittest.main()
