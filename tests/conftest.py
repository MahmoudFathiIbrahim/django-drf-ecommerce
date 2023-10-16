# this file will be read before any testing done
# here we should register or factories before make a test in any factory test
from pytest_factoryboy import register
from .factories import CategoryFactory, BrandFactory, ProductFactory

from rest_framework.test import APIClient
import pytest

register(CategoryFactory)
register(BrandFactory)
register(ProductFactory)

@pytest.fixture
def api_client():
    return APIClient
