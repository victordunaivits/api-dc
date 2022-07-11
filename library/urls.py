from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from apidc.api import viewsets as apiviewsets

route = routers.DefaultRouter()
route.register(r'herois', apiviewsets.HeroisViewSet, basename='Herois')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]
