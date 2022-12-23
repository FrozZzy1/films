from django.db import models


class Genre(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'


class Country(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'


class Movie(models.Model):
    LIST_OF_RATING_MPAA = (
        ('G', 'G'),
        ('PG', 'PG'),
        ('PG-13', 'PG_13'),
        ('R', 'R'),
        ('NC-17', 'NC_17')
    )

    title = models.TextField()
    description = models.TextField()
    subtitles = models.BooleanField(default=False)
    year = models.PositiveIntegerField()
    countries = models.ManyToManyField(Country)
    genres = models.ManyToManyField(Genre)
    fees_us = models.PositiveIntegerField(default=0)
    fees_world = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='media', blank=True)
    age = models.PositiveIntegerField(default=0)
    rating_mpaa = models.CharField(max_length=5, choices=LIST_OF_RATING_MPAA)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'