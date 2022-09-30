from django.contrib import admin

# Register your models here.
from .models import Movie, Ratings

admin.site.register(Movie)
admin.site.register(Ratings)
