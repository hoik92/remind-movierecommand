from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=100)
    genreId = models.IntegerField()

    def __str__(self):
        return "{}: {} - {}".format(self.id, self.genreId, self.name)


class Movie(models.Model):
    movieNm = models.CharField(max_length=100)
    openDt = models.CharField(max_length=100)
    audiAcc = models.IntegerField()
    image_url = models.CharField(max_length=200)
    description = models.TextField()
    genres = models.ManyToManyField(Genre, related_name='movie', blank=True)
    showTm = models.IntegerField()

    def __str__(self):
        return "{}".format(self.movieNm)


class Score(models.Model):
    content = models.CharField(max_length=100)
    score = models.IntegerField()
    movie = models.ForeignKey(Movie, related_name='scores', on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), related_name='scores', on_delete=models.CASCADE)

    def __str__(self):
        return "{}: {} - {}".format(self.movie.name, self.content, self.score)