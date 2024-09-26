from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete = models.CASCADE)
    release_date = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to = 'images/', blank =True)

    def __str__(self):
        return self.title
