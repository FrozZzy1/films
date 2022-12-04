from django.db import models


class Movie(models.Model):
    LIST_OF_RATING_MPAA  = (
        ('G', 'G'),
        ('PG', 'PG'),
        ('PG-13', 'PG_13'),
        ('R', 'R'),
        ('NC-17', 'NC_17')
    )

    title = models.TextField()
    description = models.TextField()
    subtitles = models.BooleanField(default=False)
    production_year = models.PositiveIntegerField()
    country = models.TextField()
    genre = models.TextField()
    fees_us = models.PositiveIntegerField(default=0)
    fees_world = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='media', blank=True)
    age = models.PositiveIntegerField(default=0)
    rating_mpaa = models.CharField(max_length=5, choices=LIST_OF_RATING_MPAA)

