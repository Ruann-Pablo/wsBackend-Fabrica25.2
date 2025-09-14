from django.db import models
from django.contrib.auth.models import AbstractUser


# Extendendo o modelo de usuário padrão do Django (nome, email, senha)
class User(AbstractUser):
    city = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.username

class FavoriteCity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_cities')
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    class Meta:
        unique_together = ('user', 'city', 'country')

    def __str__(self):
        return f"{self.city} - {self.country}, favoritado por {self.user.username}"