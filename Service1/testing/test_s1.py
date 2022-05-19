from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
#from random import choice
from application import Character, app
import requests_mock, json

class TestBase(TestCase):
    def create_app(self):
        return app

class TestView(TestBase):
    def test_Character_get(self):
        response = self.client.get(url_for('Character', json={("Human", 0), ("Priest", 3)}))
        self.assertEqual(response.status_code, 200) #Sort this out if there's time

class TestGet(TestBase):
    def test_get_race_role(self):
        with requests_mock.Mocker() as m:
            m.get('http://service1:5001/get/race', json={"Human": 0})
            m.get('http://service2:5002/get/role', json={"Priest": 3})
            m.post('http://service3:5003/post/Character', json={"key": {"Human": 0}, "value": {"Priest": 3}})
            response = self.client.get(url_for('Character'))
            self.assertIn(b'Human', response.data)
            #self.assertIn(b'Priest', response.data)
            #assert Character()["race"] == '{"Human": 0}'
# class TestPost(TestBase):
#     def test_post_alignment:
#         with requests_mock.Mocker() as m:
#             m.get('http://localhost:5003/post/Character', json={"key":{"Human": 0}, "value":{"Priest": 3}})
#             response = self.client.post(url_for('Character')) #data = 'jsonobject')
#             assert json.loads()