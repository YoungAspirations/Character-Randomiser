from unittest.mock import patch
from flask import url_for, request
from flask_testing import TestCase
#from random import choice
from application import Character, app
import requests_mock, json

class TestBase(TestCase):
    def create_app(self):
        return app

class TestPost(TestBase):
    def test_post_alignment(self):
        info = {"key":{"Human": 0}, "value":{"Priest": 3}}
        with requests_mock.Mocker() as m:
            m.get('http://service3:5003/post/Character', data=json.dumps(info))
            assert data == json.dumps(info)
            
            
        with patch('request.get_json') as p:
            p.return_value = {"key": {"Human", 0}, "value": {"Priest", 3}}
            Response = self.client.get(url_for('race'))
            self.assertIn(b'Human',Response.data)

class TestOutput(TestBase):
    def test_alignment(self):
        with patch('sum') as p:
            p.return_value = 1
            Response = self.client.get(url_for('Alignment'))
            self.assertIn(b'Good',Response.data)
#do post and patch etc