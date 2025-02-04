from rest_framework import serializers
from base.models import Joke,Item

class JokeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Joke
        fields='__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Item
        fields='__all__'