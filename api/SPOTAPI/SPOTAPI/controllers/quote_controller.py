import connexion
import six

from SPOTAPI.models.error import Error  # noqa: E501
from SPOTAPI.models.ingredients import Ingredients  # noqa: E501
from SPOTAPI import util


def ingredients_ingredients_iddelete(ingredients_id):  # noqa: E501
    """Delete ingredients object

    Test # noqa: E501

    :param ingredients_id: The Id of a ingredient
    :type ingredients_id: int

    :rtype: None
    """
    return 'do some magic!'


def ingredients_ingredients_idpatch(ingredients_id, ingredients):  # noqa: E501
    """Update ingredients object

    Test # noqa: E501

    :param ingredients_id: The Id of a ingredient
    :type ingredients_id: int
    :param ingredients: 
    :type ingredients: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        ingredients = Ingredients.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
