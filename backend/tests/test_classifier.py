# -*- coding: utf-8 -*-
"""Test Classifier."""
import os
import json
import warnings
from io import BytesIO

import unittest

from core.app import create_app
from core.settings import DevConfig


class TestClassifier(unittest.TestCase):
    URL = '/api/classifiers/predict/'

    def setUp(self):
        self.client = create_app(DevConfig).test_client()

    def test_should_return_bad_request_when_the_field_is_not_sent(self):
        expected = {
            'message': 'Bad Request: Missing or empty field. Please upload an image with the extension jpeg.',
            'status': 400
        }
        response = self.client.post(self.URL)
        status_code = int(response.status_code)
        data = json.loads(response.data)

        self.assertEqual(expected.get('status'), status_code)
        self.assertEqual(expected.get('status'),
                         data.get('error').get('status'))
        self.assertEqual(expected.get('message'),
                         data.get('error').get('message'))

    def test_should_return_bad_request_when_file_is_not_allowed(self):
        expected = {
            'message': 'Bad Request: Missing or empty field. Please upload an image with the extension jpeg.',
            'status': 400
        }

        with open(os.path.join('tests', 'images', 'pneumonia_bacteria_1.png'), 'rb') as img1:
            imgStringIO = BytesIO(img1.read())

        payload = {
            'image': (imgStringIO, 'pneumonia_bacteria_1.png')
        }

        response = self.client.post(
            self.URL, content_type='multipart/form-data', data=payload)
        status_code = int(response.status_code)
        data = json.loads(response.data)

        self.assertEqual(expected.get('status'), status_code)
        self.assertEqual(expected.get('status'),
                         data.get('error').get('status'))
        self.assertEqual(expected.get('message'),
                         data.get('error').get('message'))

    def test_should_return_bad_request_when_file_is_not_allowed(self):
        expected = {
            'result': {
                'prediction': 'PNEUMONIA',
                'probabilities': {
                    'NORMAL': 0.02898966334760189,
                    'PNEUMONIA': 0.9710103869438171
                },
                'success': True
            },
            'status': 200
        }

        with open(os.path.join('tests', 'images', 'pneumonia_virus_6.jpeg'), 'rb') as img1:
            imgStringIO = BytesIO(img1.read())

        payload = {
            'image': (imgStringIO, 'pneumonia_virus_6.jpeg')
        }

        response = self.client.post(
            self.URL, content_type='multipart/form-data', data=payload)
        status_code = int(response.status_code)
        data = json.loads(response.data)

        self.assertEqual(expected.get('status'), status_code)
        self.assertEqual(expected.get('result'),
                         data)
