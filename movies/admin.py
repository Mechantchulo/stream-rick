from django.contrib import admin
from .models import Movie, Genre

# Register your models here.
from django.contrib import admin
from .models import Genre, Movie

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'release_date', 'description', 'image')
    # You can also add search fields or filters if needed
