from django.db import models


class Movie(models.Model):
    LIST_OF_RATING_MPAA = (
        ('G', 'G'),
        ('PG', 'PG'),
        ('PG-13', 'PG_13'),
        ('R', 'R'),
        ('NC-17', 'NC_17')
    )

    LIST_OF_GENRES = (
        ('Боевик', 'Боевик'),
        ('Приключения', 'Приключения'),
        ('Драма', 'Драма'),
        ('Фантастика', 'Фантастика'),
        ('Триллер', 'Триллер'),
        ('Детектив', 'Детектив'),
        ('Ужасы', 'Ужасы')
    )

    title = models.TextField()
    description = models.TextField()
    subtitles = models.BooleanField(default=False)
    year = models.PositiveIntegerField()
    country = models.TextField()
    genre = models.CharField(max_length=11, choices=LIST_OF_GENRES)
    fees_us = models.PositiveIntegerField(default=0)
    fees_world = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='media', blank=True)
    age = models.PositiveIntegerField(default=0)
    rating_mpaa = models.CharField(max_length=5, choices=LIST_OF_RATING_MPAA)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class RatingStar(models.Model):
    value = models.SmallIntegerField('Значение', default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = 'Звезды рейтинга'
        verbose_name_plural = 'Звезды рейтинга'
        ordering = ['-value']


class Rating(models.Model):
    ip = models.CharField('IP адрес', max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='звезда')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='фильм')

    def __str__(self):
        return f'{self.star} - {self.movie}'

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'