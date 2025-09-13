from django.shortcuts import render
from rest_framework import viewsets
from .models import User, City, Forecast, FavoriteCity
from .serializers import UserSerializer, CitySerializer, ForecastSerializer, FavoriteCitySerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class ForecastViewSet(viewsets.ModelViewSet):
    queryset = Forecast.objects.all()
    serializer_class = ForecastSerializer

class FavoriteCityViewSet(viewsets.ModelViewSet):
    queryset = FavoriteCity.objects.all()
    serializer_class = FavoriteCitySerializer
