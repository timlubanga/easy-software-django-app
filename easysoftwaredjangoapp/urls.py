"""easysoftwaredjangoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from userAuth.urls import authurlpatterns
from loan.urls import loanurlpatterns


schema_view = get_schema_view(
    openapi.Info(
        title="Easy Software Limited",
        default_version='v1',
        description="Swagger documentation for Easy Software API using django and django restframework",
        terms_of_service="https://www.easysoftware.com/policies/terms/",
        contact=openapi.Contact(email="timlubanga@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('documentation/', schema_view.with_ui('redoc',
         cache_timeout=0), name='redoc'),
    path('auth/', include(authurlpatterns), name='auth'),
    path('loan/', include(loanurlpatterns), name='loan')
]
