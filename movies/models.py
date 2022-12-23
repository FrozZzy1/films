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


class Director(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Director'
        verbose_name_plural = 'Directors'


class Script(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Script'
        verbose_name_plural = 'Scripts'


class Producer(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Producer'
        verbose_name_plural = 'Producers'


class Composer(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Composer'
        verbose_name_plural = 'Composers'


class Artist(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Artist'
        verbose_name_plural = 'Artists'


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
    directors = models.ManyToManyField(Director)
    scripts = models.ManyToManyField(Script)
    producers = models.ManyToManyField(Producer)
    composers = models.ManyToManyField(Composer)
    artists = models.ManyToManyField(Artist)
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