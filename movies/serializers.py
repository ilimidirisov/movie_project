from rest_framework import serializers
from .models import Movie, Genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class MovieSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'release_date']

    def create(self, validated_data):
        genre_data = validated_data.pop('genre')
        genre, created = Genre.objects.get_or_create(**genre_data)
        movie = Movie.objects.create(genre=genre, **validated_data)
        return movie

    def update(self, instance, validated_data):
        genre_data = validated_data.pop('genre', None)
        if genre_data:
            genre, created = Genre.objects.get_or_create(**genre_data)
            instance.genre = genre

        instance.title = validated_data.get('title', instance.title)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.save()
        return instance
