from rest_framework import serializers
from .models import User, City, Forecast, FavoriteCity

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'city', 'password']

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            city=validated_data.get('city', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.city = validated_data.get('city', instance.city)
        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name', 'country']

class ForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forecast
        fields = ['id', 'city', 'date', 'predicted_temperature', 'predicted_humidity', 'predicted_wind_speed']

class FavoriteCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteCity
        fields = ['id', 'user', 'city']