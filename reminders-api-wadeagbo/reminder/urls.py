from django.urls import path
from rest_framework.documentation import include_docs_urls
from rest_framework import routers


from rest_framework_swagger.views import get_swagger_view
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


from .views import (
    ReminderList,
    ReminderCreate,
    ReminderDetail,
    UserList,
    UserDetail,
)


router = routers.DefaultRouter()
router.register(r"reminder", ReminderList)


schema_view = get_schema_view(
    openapi.Info(
        title="Reminder API",
        default_version="v1",
        description="API documentation for reminder app",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path("api/v1/reminder/list/", ReminderList.as_view(), name="reminder-list"),
    path("api/v1/reminder/create/", ReminderCreate.as_view(), name="reminder-create"),
    path(
        "api/v1/reminder/detail/<int:pk>/",
        ReminderDetail.as_view(),
        name="reminder-detail",
    ),
    path("api/v1/users/", UserList.as_view(), name="user-list"),
    path("api/v1/users/<int:pk>/", UserDetail.as_view(), name="user-detail"),
    # path('swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path("swagger.json/", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger.yaml/", schema_view.without_ui(cache_timeout=0), name="schema-yaml"),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
