from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import race, app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestView(TestBase):
    def test_race_get(self):
        response = self.client.get(url_for('race'))
        self.assertEqual(response.status_code, 200)

class TestOutput(TestBase):
    def test_get_race(self):
        with patch('random.choice') as p:
            p.return_value = ('Dwarf', 1)
            Response = self.client.get(url_for('race'))
            self.assertIn(b'Dwarf',Response.data)

#if statement not being read so should be 100%