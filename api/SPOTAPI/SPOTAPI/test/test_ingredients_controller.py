# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from SPOTAPI.models.ingredients import Ingredients  # noqa: E501
from SPOTAPI.test import BaseTestCase


class TestIngredientsController(BaseTestCase):
    """IngredientsController integration test stubs"""

    def test_ingredients_get(self):
        """Test case for ingredients_get

        Retrieve a collection of Quote objects
        """
        query_string = [('offset', 1),
                        ('limit', 20)]
        headers = { 
            'Accept': 'application/json',
            'ApiKeyAuth': 'special-key',
        }
        response = self.client.open(
            '/ingredients',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ingredients_ingredients_idget(self):
        """Test case for ingredients_ingredients_idget

        Retrieve a ingredient object
        """
        headers = { 
            'ApiKeyAuth': 'special-key',
        }
        response = self.client.open(
            '/ingredients/{ingredients_id}'.format(ingredients_id=1),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ingredients_post(self):
        """Test case for ingredients_post

        Create ingredients
        """
        ingredients = {}
        headers = { 
            'Content-Type': 'application/json',
            'ApiKeyAuth': 'special-key',
        }
        response = self.client.open(
            '/ingredients',
            method='POST',
            headers=headers,
            data=json.dumps(ingredients),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
