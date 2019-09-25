from django.shortcuts import render, get_object_or_404
from movies.models import Genre, Movie, Score
from .serializers import GenreSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.http import JsonResponse
import json

# Create your views here.


@api_view(['GET'])
def genre_list(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    # return Response(serializer.data)
    return JsonResponse(json.loads(json.dumps(serializer.data)), safe=False)