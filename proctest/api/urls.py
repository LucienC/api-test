from django.urls import include, path
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r'regions', views.RegionViewSet, basename='regions')

urlpatterns = [
    path('', include(router.urls)),
]
