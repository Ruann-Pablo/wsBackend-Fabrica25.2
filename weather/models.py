from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.
class User(AbstractUser):
    city = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.username

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    class Meta:
        unique_together = ('name', 'country')

    def __str__(self):
        return f"{self.name}, {self.country}"

class Forecast(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='forecasts')
    date = models.DateField()
    predicted_temperature = models.FloatField()
    predicted_humidity = models.FloatField()
    predicted_wind_speed = models.FloatField()

    def __str__(self):
        return f"Previsão do tempo para {self.city.name} em {self.date}"
    

class FavoriteCity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_cities')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='favorited_by')

    class Meta:
        unique_together = ('user', 'city')

    def __str__(self):
        return f"{self.city.name} favoritado por {self.user.username}"