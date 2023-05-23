from django.urls import path
from .views import list_api, list_view, new_feedback

urlpatterns = [
    path("", list_view, name="list"),
    path("api/feedback/", list_api, name="api_list"),    
    path("new/", new_feedback, name="new_feedback")
]
