from rest_framework import serializers
from movies.models import Genre, Movie, Score


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name', 'genreId',]