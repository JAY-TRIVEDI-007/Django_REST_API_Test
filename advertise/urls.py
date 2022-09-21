from django.urls import path, include
from .views import AdListCreateAPIView, AdRetrieveUpdateDeleteAPIView


urlpatterns = [
    # path('ads', create_ad)
    path('ads/<int:adID>/', AdRetrieveUpdateDeleteAPIView.as_view()),
    path('ads/', AdListCreateAPIView.as_view())
]
