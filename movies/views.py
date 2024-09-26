from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Genre, Movie
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView

# View for the homepage
class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        """
        Provides context data for the home page. 
        - Retrieves all genres and the first 10 movies.
        """
        context = super().get_context_data(**kwargs)
        context['genres'] = Genre.objects.all()  # Fetch all genres
        context['movies'] = Movie.objects.all()[:10]  # Fetch the first 10 movies
        return context

# View for search results
class SearchResultsView(TemplateView):
    template_name = 'search_results.html'

    def get_queryset(self):
        """
        Filters movies and genres based on the search query from the GET request.
        - Retrieves the search query parameter 'q'.
        - Returns filtered movie and genre results as a dictionary.
        """
        query = self.request.GET.get('q', '')  # Get the search query
        movie_results = Movie.objects.filter(title__icontains=query)  # Search movies by title
        genre_results = Genre.objects.filter(name__icontains=query)  # Search genres by name
        return {
            'movies': movie_results,
            'genres': genre_results,
            'query': query  # Include the search query in the context
        }

    def get_context_data(self, **kwargs):
        """
        Provides context data for search results page.
        - Updates context with search results and query.
        """
        context = super().get_context_data(**kwargs)
        context.update(self.get_queryset())  # Add search results to context
        return context

# View for listing all genres
class GenreListView(ListView):
    model = Genre
    template_name = 'genre_list.html'
    context_object_name = 'genres'  # The list of genres will be accessible as 'genres' in the template

# View for showing details of a specific genre
class GenreDetailView(DetailView):
    model = Genre
    template_name = 'genre_detail.html'

# View for listing all movies
class MovieListView(ListView):
    model = Movie
    template_name = 'movie_list.html'
    context_object_name = 'movies'  # The list of movies will be accessible as 'movies' in the template

# View for showing details of a specific movie
class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie_detail.html'

