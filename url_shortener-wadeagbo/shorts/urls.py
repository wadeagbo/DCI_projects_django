from django.urls import path
from .views import index, url_redirect, url_list

urlpatterns = [
    path('', index, name='index'),
    path('url/<str:shortened>/', url_redirect, name='url_redirect'),
    path('urls/', url_list, name='url_list'),
]