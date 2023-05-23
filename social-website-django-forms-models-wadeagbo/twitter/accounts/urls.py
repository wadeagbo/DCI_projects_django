from django.urls import path
from django.views.generic import TemplateView
from .views import ProfileView

urlpatterns = [
    path("profile/", ProfileView.as_view(), name='profile'),    
]
