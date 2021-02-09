import connexion
import six

from SPOTAPI.models.recipes import Recipes  # noqa: E501
from SPOTAPI import util


def recipe_get(offset=None, limit=None):  # noqa: E501
    """Retrieve a collection of recipe objects

    This operation supports pagination # noqa: E501

    :param offset: The number of items to skip before returning the results
    :type offset: int
    :param limit: The number of items to return
    :type limit: int

    :rtype: None
    """
    return 'do some magic!'


def recipe_post(recipes):  # noqa: E501
    """Create recipes

     # noqa: E501

    :param recipes: 
    :type recipes: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        recipes = Recipes.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
