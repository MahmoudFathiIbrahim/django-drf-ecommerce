import factory
from product.models import Category, Brand, Product

# here we should create the factory test which collect all the metadata and prepare it for test


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
    # this to return ouput of name = 'test_category'
    # name = 'test_category' # when test endpoint by adding 3 records it will raise error cuz it should be unique
    # this to create sequence start from 0 when create more than one record in the database
    name = factory.Sequence(lambda n: f'Category_{n}')


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    # name = 'test_brand'
    name = factory.Sequence(lambda n: f'Brand_{n}')


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    # we should build brand and category before product because the product is in relationship with both

    name = 'test_product'
    description = 'test_description'
    is_digital = True
    brand = factory.SubFactory(BrandFactory)
    category = factory.SubFactory(CategoryFactory)
