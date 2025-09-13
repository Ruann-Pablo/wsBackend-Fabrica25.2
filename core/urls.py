from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from weather.views import UserViewSet, CityViewSet, ForecastViewSet, FavoriteCityViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'cities', CityViewSet)
router.register(r'forecasts', ForecastViewSet)
router.register(r'favorites', FavoriteCityViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
