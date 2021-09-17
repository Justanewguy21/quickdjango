from django.http import response
from django.shortcuts import render
from .models import Movie
# Create a home page views here.
# this is the home page of movieapp
def home(request):
    # movie_data = [
    #     {
    #         'name': 'john wich 1',
    #         'description': 'sjkhdaskjhda',
    #         'year': 2014
    #     },
    #     {
    #         'name': 'The Shawshank Redemption',
    #         'description': 'sjkhdaskjhda',
    #         'year': 1994
            
    #     },
    # ]
    movie_data = Movie.objects.all()
    return render(request, 'home.html', {'movies':movie_data})
# testimonials
def testimonials(request):
    return render(request, 'testimonials.html', {})
def movie(request, movieid):
    movie_record = Movie.objects.get(id = movieid)

    return render(request, 'movie.html', {'movie': movie_record})

    
