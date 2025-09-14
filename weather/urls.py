from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, FavoriteCityViewSet, WeatherAPIView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'weather/history', FavoriteCityViewSet, basename='favorite_city')

urlpatterns = [
    path('', include(router.urls)),
    path('weather/', WeatherAPIView.as_view(), name='weather'),  # GET para consultar clima
]
