from django_filters import rest_framework as filters
from .models import Movie


class MovieFilter(filters.FilterSet):
    genre = filters.CharFilter()
    country = filters.CharFilter()
    year = filters.RangeFilter()

    class Meta:
        model = Movie
        fields = ['genre', 'country', 'year']