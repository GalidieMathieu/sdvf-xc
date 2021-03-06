# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from SPOTAPI.models.base_model_ import Model
from SPOTAPI.models.diet import Diet
from SPOTAPI import util

from SPOTAPI.models.diet import Diet  # noqa: E501

class DietUser(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, allergie=None, ingredient=None):  # noqa: E501
        """DietUser - a model defined in OpenAPI

        :param allergie: The allergie of this DietUser.  # noqa: E501
        :type allergie: bool
        :param ingredient: The ingredient of this DietUser.  # noqa: E501
        :type ingredient: Diet
        """
        self.openapi_types = {
            'allergie': bool,
            'ingredient': Diet
        }

        self.attribute_map = {
            'allergie': 'allergie',
            'ingredient': 'ingredient'
        }

        self._allergie = allergie
        self._ingredient = ingredient

    @classmethod
    def from_dict(cls, dikt) -> 'DietUser':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DietUser of this DietUser.  # noqa: E501
        :rtype: DietUser
        """
        return util.deserialize_model(dikt, cls)

    @property
    def allergie(self):
        """Gets the allergie of this DietUser.


        :return: The allergie of this DietUser.
        :rtype: bool
        """
        return self._allergie

    @allergie.setter
    def allergie(self, allergie):
        """Sets the allergie of this DietUser.


        :param allergie: The allergie of this DietUser.
        :type allergie: bool
        """
        if allergie is None:
            raise ValueError("Invalid value for `allergie`, must not be `None`")  # noqa: E501

        self._allergie = allergie

    @property
    def ingredient(self):
        """Gets the ingredient of this DietUser.


        :return: The ingredient of this DietUser.
        :rtype: Diet
        """
        return self._ingredient

    @ingredient.setter
    def ingredient(self, ingredient):
        """Sets the ingredient of this DietUser.


        :param ingredient: The ingredient of this DietUser.
        :type ingredient: Diet
        """

        self._ingredient = ingredient
