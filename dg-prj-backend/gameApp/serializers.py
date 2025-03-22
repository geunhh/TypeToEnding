from rest_framework import serializers
from .models import Movie, GameRecord, InitialQuestion, Comment
from accounts.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["name"]


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class GameRecordSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)  # Movie를 중첩 Serializer로 처리

    class Meta:
        model = GameRecord
        fields = "__all__"


class InitialQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InitialQuestion
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ["created_at", "updated_at", "user", "movie"]
