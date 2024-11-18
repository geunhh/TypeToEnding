from rest_framework import serializers
from .models import Movie, GameRecord

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class GameRecordSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)  # Movie를 중첩 Serializer로 처리
    class Meta:
        model = GameRecord
        fields = '__all__'
