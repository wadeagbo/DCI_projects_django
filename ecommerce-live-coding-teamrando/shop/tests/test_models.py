from rest_framework.test import APITestCase

# Create your tests here.
"""
APISimpleTestCase
APITransactionTestCase
APITestCase ---> use today
APILiveServerTestCase
"""
# CRUD -> Create, Delete, Listing of products, Update

from shop.models import Product

product_schema = {
    "name": "Some glorious name",
    "description": "Get ripped!!",
    "price": 19.99,
}


class ProductCreateTest(APITestCase):
    def test_create_product(self):
        # count how many products did we have before?
        initial_count = Product.objects.count()
        # send a POST request to the client/server
        response = self.client.post("/api/v1/products/create/", product_schema)
        # response = self.client.post("/api/v1/products/create", {
        #     "name": "Some glorious name",
        #     "description": "Get ripped!!",
        #     "price": 19.99
        # })
        self.assertEqual(Product.objects.count(), initial_count + 1)

        for attr, value in product_schema.items():
            self.assertEqual(response.data[attr], value)


class ProductDeleteTest(APITestCase):
    def setUp(self) -> None:
        self.product = Product.objects.create(**product_schema)

    def test_delete(self):
        initial_count = Product.objects.count()  # 10
        product = Product.objects.first()  # ORM method that get any first product
        response = self.client.delete(f"/api/v1/products/{product.id}/")
        self.assertEqual(response.status_code, 204)
        # Question: Test the initial count versus the total product count
        self.assertEqual(initial_count - 1, Product.objects.count())

        # does the product exist anymore?
        self.assertRaises(Product.DoesNotExist, Product.objects.get, id=self.product.id)


class ProductListTest(APITestCase):
    def test_list_products(self):
        product_count = Product.objects.count()
        response = self.client.get("/api/v1/products/")  # Paginated!!
        self.assertIsNone(response.data["next"])
        self.assertIsNone(response.data["previous"])
        self.assertEqual(product_count, response.data["count"])
        self.assertEqual(product_count, len(response.data["results"]))


class ProductUpdateTest(APITestCase):
    def setUp(self) -> None:
        Product.objects.create(**product_schema)

    def test_update_product(self):
        product = Product.objects.first()
        product_name = "Berlin Icecream"
        # confirm that the name has not not changed
        self.assertEqual(product.name, product_schema["name"])
        # update with a patch
        # HTTP verbs
        # - GET, DELETE, POST, PUT, PATCH
        response = self.client.patch(
            f"/api/v1/products/{product.id}/",
            {"name": product_name},
            format="json",
        )
        updated_product = Product.objects.get(id=product.id)
        self.assertEqual(updated_product.name, product_name)
        self.assertEqual(response.data['name'], product_name)
