from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("books.urls")),

    # OpenAPI схема
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),

    # Swagger через CDN
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema", template_name=None), name="swagger-ui"),
]