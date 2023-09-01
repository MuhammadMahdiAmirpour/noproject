from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Movies
# from django.views.generic import ListView
# Create your views here.

# class MovieList(ListView):
#     model = Movies
#     template_name = 'newapp/movie_list.html'
#     context_object_name = 'movie_objects'
#     paginate_by = 10
#     paginate_orphans

def movie_list(request):
    movie_objects = Movies.objects.all()

    movie_name = request.GET.get('movie_name')
    
    if all([movie_name != '', movie_name != None]):
        movie_objects = movie_objects.filter(name__icontains=movie_name)

    paginator = Paginator(movie_objects, 2)
    page = request.GET.get('page')
    movie_objects = paginator.get_page(page)
    return render(request, 'newapp/movie_list.html', {'movie_objects': movie_objects})

