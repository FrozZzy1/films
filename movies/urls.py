from django.urls import path

from .views import MovieListAPIView, MovieRetrieveDestroyAPIView, GenreListAPIView

urlpatterns = [
    path('', MovieListAPIView.as_view()),
    path('genres/', GenreListAPIView.as_view()),
    path('<int:pk>', MovieRetrieveDestroyAPIView.as_view()),

]
