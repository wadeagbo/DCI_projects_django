from django.urls import path 
from  .views import about_view,base_view 
from myapp.views import HomePageView, AboutPageView


urlpatterns = [
    path("", about_view, name="about_F"),
    path("base/", base_view, name="base"),
    path("about_using_class/", AboutPageView.as_view(), name="about_C" ),
    path("home/", HomePageView.as_view(), name="home_C")
]
