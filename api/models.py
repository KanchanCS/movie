from django.db import models

# Create your models here.


class Movie(models.Model):
    tconst = models.CharField(max_length=14, unique=True)
    titleType = models.CharField(max_length=100)
    primary_title = models.CharField(max_length=150)
    runtime = models.IntegerField(default=0)
    genres = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.primary_title


class Ratings(models.Model):
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, blank=True, default=None)
    tconst = models.CharField(max_length=14, unique=True)
    avg_rating = models.DecimalField(
        default=0.0, max_digits=4, decimal_places=3)
    votes = models.IntegerField()

    def __str__(self) -> str:
        return self.movie.primary_title
