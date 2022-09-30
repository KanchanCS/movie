from django.http import JsonResponse

from .models import Movie, Ratings

# Create your views here.


def longest_duration_movies(request):
    # retrive the high durations movies top 10
    largest_runtime = (Movie.objects.all()
                       .order_by('-runtime')
                       [:10])
    result = {}
    for movie in largest_runtime:
        data = {movie.id: {
                'tconst': movie.tconst,
                'name': movie.primary_title,
                'runtime': movie.runtime,
                'genres': movie.genres

                }}
        print(data)
        result.update(data)
    return JsonResponse(result)


def top_rated_movies(request):
    top_rated_movies = Ratings.objects.filter(
        avg_rating__gte=6.6
    ).order_by('-avg_rating')
    result = {}
    for movie in top_rated_movies:
        data = {movie.movie.id: {
                'tconst': movie.tconst,
                'name': movie.movie.primary_title,
                'runtime': movie.movie.runtime,
                'genres': movie.movie.genres,
                'avg_rating': movie.avg_rating,

                }}
        result.update(data)

    return JsonResponse(result)
