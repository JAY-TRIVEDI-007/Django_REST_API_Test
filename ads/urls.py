from django.urls import path
from .views import create_ad


urlpatterns = [
    path('ads', create_ad)
]
