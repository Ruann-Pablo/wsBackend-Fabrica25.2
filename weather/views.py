from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import User, FavoriteCity
from .serializers import UserSerializer, FavoriteCitySerializer
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
import requests

class IsSelf(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)
    
    def perform_create(self, serializer):
        return serializer.save()

    def get_permissions(self):
        if self.action == "create":  
            return [AllowAny()]  
        return [IsAuthenticated()]

class FavoriteCityViewSet(viewsets.ModelViewSet):
    serializer_class = FavoriteCitySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return FavoriteCity.objects.filter(user=self.request.user)

    def create_from_weather(self, user, city, country):
        favorite, created = FavoriteCity.objects.get_or_create(user=user, city=city, country=country)
        return favorite, created


class WeatherAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        city = request.query_params.get('city')
        if not city:
            return Response({"error": "O parâmetro da cidade é obrigatório."}, status=status.HTTP_400_BAD_REQUEST)

        api_key = settings.OPENWEATHER_API_KEY
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=pt_br"


        response = requests.get(url)
        if response.status_code != 200:
            return Response({"error": "Não foi possível buscar os dados do tempo."}, status=response.status_code)

        data = response.json()

        favorite_city = FavoriteCityViewSet().create_from_weather(
            city=data["name"], 
            country=data["sys"]["country"], 
            user=request.user
        )

        weather_data = {
            "cidade": data["name"],
            "pais": data["sys"]["country"],
            "temperatura": data["main"]["temp"],
            "descricao": data["weather"][0]["description"],
        }

        if not favorite_city:
            FavoriteCityViewSet().create_from_weather(request.user, weather_data["cidade"], weather_data["pais"])

        return Response(weather_data, status=status.HTTP_200_OK)