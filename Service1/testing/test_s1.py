from unittest.mock import patch
from flask import url_for, jsonify
from flask_testing import TestCase
from application import Character, app
import requests_mock, json

class TestBase(TestCase):
    def create_app(self):
        return app

class TestGet(TestBase):
    def test_get_Character(self):
        with requests_mock.Mocker() as m:
            a = m.get('http://service2:5001/get/race', json={'Human': 0})
            b = m.get('http://service3:5002/get/role', json={'Priest': 3})
            c = m.post('http://service4:5003/post/Character', json={"moral": "Good"})
            response = self.client.get(url_for('Character'))
            self.assertIn(b'Good', response.data)
            self.assertIn(b'Human', response.data)
          
# class TestPost(TestBase):
#     def test_post_alignment:
#         with requests_mock.Mocker() as m:
#             m.get('http://localhost:5003/post/Character', json={"key":{"Human": 0}, "value":{"Priest": 3}})
#             response = self.client.post(url_for('Character')) #data = 'jsonobject')
#             assert json.loads()