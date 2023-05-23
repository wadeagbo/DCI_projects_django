from django.db import models
from django.utils import timezone


class Product(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()
    price = models.FloatField()
    photo = models.ImageField(
        blank=True, null=True, default=None, upload_to="uploads/products"
    )

    # def get_forex_price(self):
    #     # reach an API and get the forex
    #     return

    def get_rounded_price(self):
        return round(self.price, 2)

    def __repr__(self) -> str:
        return f"<Product {self.id} {self.name}>"

    def __str__(self) -> str:
        return f"<Product id={self.id} name={self.name}>"


class Cart(models.Model):
    TAX_RATE = 0.19  # 19% VAT

    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def subtotal(self):
        return round(
            sum(
                [
                    item.quantity * item.product.get_price()
                    for item in self.shopping_cart_items
                ]
            ),
            2,
        )

    def taxes(self):
        return round(self.TAX_RATE * self.subtotal(), 2)

    def total(self):
        return round(self.subtotal() * self.taxes(), 2)


class LineItem(models.Model):
    cart = models.ForeignKey(
        Cart, related_name="items", related_query_name="item", on_delete=models.CASCADE
    )
    product = models.ForeignKey(Product, related_name="+", on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def total(self):
        return round(self.quantity * self.product.get_rounded_price())

    def __repr__(self) -> str:
        return f'<Cart {self.id} Qty: {self.quantity} "{self.product.name}"'
