from django.contrib import admin

from movies.models import Movie, Genre, Country, Director, Script, Producer, Composer, Painter, Starring, RolesDubbed

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Country)
admin.site.register(Director)
admin.site.register(Script)
admin.site.register(Producer)
admin.site.register(Composer)
admin.site.register(Painter)
admin.site.register(Starring)
admin.site.register(RolesDubbed)
