from django.urls import path
from .views import (
    show,
    cart,
    index,
    ProductList,
    ProductCreate,
    ProductGetUpdateDestroy,
    # ProductDestroy,
    # ProductDetail,
    # ProductUpdate,
)

urlpatterns = [
    path("api/v1/products/create/", ProductCreate.as_view()),
    # path("api/v1/products/delete/<int:pk>/", ProductDestroy.as_view()),
    # path("api/v1/products/detail/<int:pk>/", ProductDetail.as_view()),
    # path("api/v1/products/update/<int:pk>/", ProductUpdate.as_view()),
    path("api/v1/products/<int:pk>/", ProductGetUpdateDestroy.as_view()),
    path("api/v1/products/", ProductList.as_view()),
    path("products/<int:pk>/", show, name="product-detail"),
    path("cart/", cart, name="cart"),
    path("", index, name="product-list"),
]


# CRUD
# C - create (POST)
# R - read (Listview, RetrieveAPIView / conventional django -> DETAIL view )
# U - (x)
# D - DestroyAPIView
