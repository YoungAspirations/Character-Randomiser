from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import role, app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestView(TestBase):
    def test_role_get(self):
        response = self.client.get(url_for('role'))
        self.assertEqual(response.status_code, 200)

class TestOutput(TestBase):
    def test_get_role(self):
        with patch('random.choice') as p:
            p.return_value = ('Sorcerer', 0)
            Response = self.client.get(url_for('role'))
            self.assertIn(b'{"Sorcerer":0}',Response.data)

        