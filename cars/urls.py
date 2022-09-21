from django.urls import path, include
from .views import CarCreateListAPIView, CarRetrieveUpdateDestroyAPIView


urlpatterns = [
    # path('cars', create_car)
    path('cars/<int:carID>/', CarRetrieveUpdateDestroyAPIView.as_view()),
    path('cars/', CarCreateListAPIView.as_view()),
]
