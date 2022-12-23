from rest_framework import serializers

from movies.models import Movie, Genre, Country


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id',
                  'title',
                  ]


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id',
                  'title',
                  ]


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    countries = CountrySerializer(many=True)

    class Meta:
        model = Movie
        fields = ['id',
                  'title',
                  'description',
                  'subtitles',
                  'year',
                  'countries',
                  'genres',
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
                  'year',
                  'countries',
                  'genres',
                  'fees_us',
                  'fees_world',
                  'image',
                  ]



