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
        response = self.client.post(url_for('Character'),json={"key": {"Human", 0}, "value": {"Priest", 3}})
        self.assertEqual(response.status_code, 200)

class TestPost(TestBase):
    def test_post_alignment:
        with requests_mock.Mocker() as m:
            m.get('http://service3:5003/post/Character', json={"key":{"Human": 0}, "value":{"Priest": 3}})
            response = self.client.post(url_for('Character')) #data = 'jsonobject')
            assert json.loads()
#do post and patch etc