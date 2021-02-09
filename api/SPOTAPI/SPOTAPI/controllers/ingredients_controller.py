import connexion
import six

from SPOTAPI.models.ingredients import Ingredients  # noqa: E501
from SPOTAPI import util


def ingredients_get(offset=None, limit=None):  # noqa: E501
    """Retrieve a collection of Quote objects

    This operation supports pagination # noqa: E501

    :param offset: The number of items to skip before returning the results
    :type offset: int
    :param limit: The number of items to return
    :type limit: int

    :rtype: None
    """
    return 'do some magic!'


def ingredients_ingredients_idget(ingredients_id):  # noqa: E501
    """Retrieve a ingredient object

    Test # noqa: E501

    :param ingredients_id: The Id of a ingredient
    :type ingredients_id: int

    :rtype: None
    """
    return 'do some magic!'


def ingredients_post(ingredients):  # noqa: E501
    """Create ingredients

     # noqa: E501

    :param ingredients: 
    :type ingredients: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        ingredients = Ingredients.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
