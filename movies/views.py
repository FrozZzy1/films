from requests import Response
from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView

from .models import Movie, Genre
from .serializers import MovieSerializer, MovieDetailSerializer, GenreSerializer


#получение списка всех фильмов
class MovieListAPIView(ListAPIView):
    serializer_class = MovieSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ['genres__title', 'countries__title', 'year']
    queryset = Movie.objects.all()
    search_fields = ['title']


#получение и удаление конкретного фильма
class MovieRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer


#получение списка всех жанров
class GenreListAPIView(ListAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


#добавление фильма в избранное
class FavoritesAPIView(APIView):
    def post(self, request):
        return Response()

