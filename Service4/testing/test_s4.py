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
        response = self.client.post(url_for('Character'), json ={"key":{"Human": 0}, "value":{"Priest": 3}})
        self.assertEqual(response.status_code, 200)
            
class TestOutputGood(TestBase):
    def test_alignment_good(self):
        response = self.client.post(
            url_for('Character'),
            json = {"key":{"Human": 0}, "value":{"Priest": 3}})
        self.assertIn(b'Good',response.data)

class TestOutputBad(TestBase):
    def test_alignment_bad(self):
        response = self.client.post(
            url_for('Character'),
            json = {"key":{"Human": 0}, "value":{"Necromancer": -3}})
        self.assertIn(b'Bad',response.data)


class TestOutputNeutral(TestBase):
    def test_alignment_neutral(self):
        response = self.client.post(
            url_for('Character'),
            json = {"key":{"Human": 0}, "value":{"Warrior": 0}})
        self.assertIn(b'Neutral',response.data)
#Test web hook