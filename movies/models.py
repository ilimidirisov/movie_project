from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='movies')
    release_date = models.DateField()

    def __str__(self):
        return self.title
