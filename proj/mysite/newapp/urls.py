from django.urls import path
from .views import movie_list

app_name = "newapp"
urlpatterns = [
    path('movies/', movie_list, name="movie_list"),
]

