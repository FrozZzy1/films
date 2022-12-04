from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView

from movies.models import Movie
from movies.serializers import MovieSerializer, MovieDetailSerializer


class MovieListAPIView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer
