""""

- Page Number pagination 

<1, 2,3,4,5.... 11242>

- Limit Offset pagination 
"limit" - controls how many items show up on a page
offset -> controlls which page we are on.

- Cursor Pagination 
"cursor" ?? DB API
"""

from django.shortcuts import render
from .models import Product, Cart

# black
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    DestroyAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .serializer import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.exceptions import ValidationError


def show(request, pk):
    context = {"product": Product.objects.get(pk=pk)}
    return render(request, "shop/product.html", context)


def cart(request):
    context = {
        "items": [],
        "subtotal": 1,
        "tax_rate": int(Cart.TAX_RATE * 100),
        "tax_total": 2.0,
        "total": 3,
    }
    return render(request, "shop/cart.html", context)


def index(request):
    products = Product.objects.all()
    return render(
        request,
        "shop/product_list.html",
        {"products": products, "number_of_products": products.count()},
    )


# API views below - yes or no
class PaginatedProducts(LimitOffsetPagination):
    # 2 attributes
    default_limit = 10
    max_limit = 100  # max size of the page that can be set by the API client


class ProductList(ListAPIView):
    # 3 attributes
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # filter
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ("name", "description")
    filterset_fields = ("id",)
    pagination_class = PaginatedProducts


class ProductCreate(CreateAPIView):
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        try:
            price = request.data.get("price")
            if not price and float(price) <= 0.0:
                raise ValidationError({"price": "Price must be above €0"})
        except ValueError:
            raise ValidationError({"price": "Price must be a number"})
        return super().create(request, *args, **kwargs)


# class ProductDestroy(DestroyAPIView):
#     queryset = Product.objects.all()


# class ProductDetail(RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# class ProductUpdate(UpdateAPIView):
#     serializer_class = ProductSerializer
#     queryset = Product.objects.all()


class ProductGetUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # def update(self, request, *args, **kwargs):
    #     response = super().update(request, *args, **kwargs)
    #     if response.status_code == 200:
    #         # customize!!
