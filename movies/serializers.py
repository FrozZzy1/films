from rest_framework import serializers

from movies.models import Movie, Genre, Country, Script, Director, Producer, Composer, Artist


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


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id',
                  'title',
                  ]


class ScriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Script
        fields = ['id',
                  'title',
                  ]


class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = ['id',
                  'title',
                  ]


class ComposerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Composer
        fields = ['id',
                  'title',
                  ]


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id',
                  'title',
                  ]


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    countries = CountrySerializer(many=True)
    directors = DirectorSerializer(many=True)
    scripts = ScriptSerializer(many=True)
    producers = ProducerSerializer(many=True)
    composers = ComposerSerializer(many=True)
    artists = ArtistSerializer(many=True)

    class Meta:
        model = Movie
        fields = ['id',
                  'title',
                  'description',
                  'subtitles',
                  'year',
                  'countries',
                  'genres',
                  'directors',
                  'scripts',
                  'producers',
                  'composers',
                  'artists',
                  'fees_us',
                  'fees_world',
                  'image',
                  'age',
                  'rating_mpaa',
                  ]


class MovieDetailSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    countries = CountrySerializer(many=True)
    directors = DirectorSerializer(many=True)
    scripts = ScriptSerializer(many=True)
    producers = ProducerSerializer(many=True)
    composers = ComposerSerializer(many=True)
    artists = ArtistSerializer(many=True)

    class Meta:
        model = Movie
        fields = ['id',
                  'title',
                  'description',
                  'subtitles',
                  'year',
                  'countries',
                  'genres',
                  'directors',
                  'scripts',
                  'producers',
                  'composers',
                  'artists',
                  'fees_us',
                  'fees_world',
                  'image',
                  ]



