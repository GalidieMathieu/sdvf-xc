# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from SPOTAPI.models.recipes import Recipes  # noqa: E501
from SPOTAPI.test import BaseTestCase


class TestRecipeController(BaseTestCase):
    """RecipeController integration test stubs"""

    def test_recipe_get(self):
        """Test case for recipe_get

        Retrieve a collection of recipe objects
        """
        query_string = [('offset', 1),
                        ('limit', 20)]
        headers = { 
            'Accept': 'application/json',
            'ApiKeyAuth': 'special-key',
        }
        response = self.client.open(
            '/recipe',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_recipe_post(self):
        """Test case for recipe_post

        Create recipes
        """
        recipes = {}
        headers = { 
            'Content-Type': 'application/json',
            'ApiKeyAuth': 'special-key',
        }
        response = self.client.open(
            '/recipe',
            method='POST',
            headers=headers,
            data=json.dumps(recipes),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
