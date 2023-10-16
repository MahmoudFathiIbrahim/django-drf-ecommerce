# here is our unit test

import pytest

pytestmark = pytest.mark.django_db


class TestCategory:
    def test_str_method(self, category_factory):
        # this category_factory() is returned from factories file which we can use its configuration or edit it
        x = category_factory(name='test_categorys')
        assert x.__str__() == 'test_categorys'


class TestBrand:
    def test_str_method(self, brand_factory):
        # this brand_factory() is returned from factories file which we can use its configuration or edit it
        x = brand_factory(name='test_brands')
        assert x.__str__() == 'test_brands'


class TestProduct:
    def test_str_method(self, product_factory):
        # this product_factory() is returned from factories file which we can use its configuration or edit it
        x = product_factory()
        assert x.__str__() == 'test_product'
