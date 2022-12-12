from django.contrib import admin

from movies.models import Movie, Rating, RatingStar

admin.site.register(Movie)
admin.site.register(RatingStar)
admin.site.register(Rating)
