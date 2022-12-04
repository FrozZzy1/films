from rest_framework import serializers

from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id',
                  'title',
                  'description',
                  'subtitles',
                  'production_year',
                  'country',
                  'genre',
                  'fees_us',
                  'fees_world',
                  'image',
                  'age',
                  'rating_mpaa',
                  ]

class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id',
                  'title',
                  'description',
                  'subtitles',
                  'production_year',
                  'country',
                  'genre',
                  'fees_us',
                  'fees_world',
                  'image',
                  ]