from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView, Response

from .models import Movie
from .serializers import MovieSerializer, MovieDetailSerializer, CreateRatingSerializer
from .service import MovieFilter


class MovieListAPIView(ListAPIView):
    serializer_class = MovieSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_class = MovieFilter
    queryset = Movie.objects.all()


class MovieRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer


class SearchMovie(ListAPIView):
    paginate_by = 32

    def get_queryset(self):
        return Movie.objects.filter(title__incontains=self.request.GET.get('search'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['search'] = self.request.GET.get('search')

        return context


class AddStarRatingAPIView(APIView):
    def get_cliend_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split('.')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        return ip

    def post(self, request):
        serializer = CreateRatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(ip=self.get_cliend_ip(request))
            return Response(status=201)
        return Response(status=400)


