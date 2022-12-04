from django.urls import path

from movies.views import MovieListAPIView, MovieRetrieveDestroyAPIView

urlpatterns = [
    path('', MovieListAPIView.as_view()),
    path('<int:pk>', MovieRetrieveDestroyAPIView.as_view()),

]
