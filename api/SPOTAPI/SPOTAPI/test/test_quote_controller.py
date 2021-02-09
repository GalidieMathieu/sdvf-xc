# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from SPOTAPI.models.error import Error  # noqa: E501
from SPOTAPI.models.ingredients import Ingredients  # noqa: E501
from SPOTAPI.test import BaseTestCase


class TestQuoteController(BaseTestCase):
    """QuoteController integration test stubs"""

    def test_ingredients_ingredients_iddelete(self):
        """Test case for ingredients_ingredients_iddelete

        Delete ingredients object
        """
        headers = { 
            'Accept': 'application/json',
            'ApiKeyAuth': 'special-key',
        }
        response = self.client.open(
            '/ingredients/{ingredients_id}'.format(ingredients_id=1),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ingredients_ingredients_idpatch(self):
        """Test case for ingredients_ingredients_idpatch

        Update ingredients object
        """
        ingredients = {}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'ApiKeyAuth': 'special-key',
        }
        response = self.client.open(
            '/ingredients/{ingredients_id}'.format(ingredients_id=1),
            method='PATCH',
            headers=headers,
            data=json.dumps(ingredients),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
