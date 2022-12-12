from django.urls import path

from .views import MovieListAPIView, MovieRetrieveDestroyAPIView, SearchMovie, AddStarRatingAPIView

urlpatterns = [
    path('', MovieListAPIView.as_view()),
    path('search/', SearchMovie.as_view(), name='search'),
    path('rating/', AddStarRatingAPIView.as_view(), name='rating'),
    path('<int:pk>', MovieRetrieveDestroyAPIView.as_view()),

]
