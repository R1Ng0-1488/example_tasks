from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path


schema_view = get_schema_view(
   openapi.Info(
      title="Example Task API",
      default_version='v1',
      description="Example Task description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="artemmaleev156@gmail.com")
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]