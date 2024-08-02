from django.urls import path
from movies.views import MovieListView, MovieDetailView

urlpatterns = [
    path("api/movies/", MovieListView.as_view(), name="movie-list"),
    path("api/movies/<int:pk>/", MovieDetailView.as_view(), name="movie-detail"),
]
