from django.urls import path
from django.contrib.auth.views import LoginView


#Import the movie Views


from .views import (
    HomePageView,
    GenreListView,
    GenreDetailView,
    MovieListView,
    MovieDetailView,
    SearchResultsView,
    
)

app_name = 'movies'

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('movies/', MovieListView.as_view(), name = 'movie_list'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name = 'movie_detail'),
    path('genres/', GenreListView.as_view(), name = 'genre_list'),
    path('genres/<int:pk>/', GenreDetailView.as_view(), name = 'genre_detail'),
    path('search/', SearchResultsView.as_view(), name = 'search_result'),
    path('login/', LoginView.as_view(template_name = 'templates/registration/login.html'), name = 'login'),
]