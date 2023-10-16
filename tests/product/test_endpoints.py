import pytest
import json

pytestmark = pytest.mark.django_db



class TestCategoryEndpoint:
    endpoint = '/api/category/'

    def test_category_get(self, category_factory, api_client):
        # .create_batch(4): it will create 4 records in our database
        category_factory.create_batch(4)

        response = api_client().get(self.endpoint)

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4


class TestBrandEndpoint:
    endpoint = '/api/brand/'

    def test_brand_get(self, brand_factory, api_client):
        # .create_batch(4): it will create 4 records in our database
        brand_factory.create_batch(4)

        response = api_client().get(self.endpoint)

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4


class TestProductEndpoint:
    endpoint = '/api/product/'

    def test_product_get(self, product_factory, api_client):
        # .create_batch(4): it will create 4 records in our database
        product_factory.create_batch(4)

        response = api_client().get(self.endpoint)

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4

