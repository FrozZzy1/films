from rest_framework import serializers

from movies.models import Movie, Genre, Country, Script, Director, Producer, Composer, Painter, Starring, RolesDubbed


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


class PainterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Painter
        fields = ['id',
                  'title',
                  ]


class StarringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Starring
        fields = ['id',
                  'title',
                  ]


class RolesDubbedSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolesDubbed
        fields =['id',
                 'title',
                 ]


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    countries = CountrySerializer(many=True)
    directors = DirectorSerializer(many=True)
    scripts = ScriptSerializer(many=True)
    producers = ProducerSerializer(many=True)
    composers = ComposerSerializer(many=True)
    painters = PainterSerializer(many=True)
    starring = StarringSerializer(many=True)
    roles_dubbed = RolesDubbedSerializer(many=True)

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
                  'painters',
                  'fees_us',
                  'fees_world',
                  'image',
                  'age',
                  'rating_mpaa',
                  'starring',
                  'roles_dubbed',
                  ]


class MovieDetailSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    countries = CountrySerializer(many=True)
    directors = DirectorSerializer(many=True)
    scripts = ScriptSerializer(many=True)
    producers = ProducerSerializer(many=True)
    composers = ComposerSerializer(many=True)
    painters = PainterSerializer(many=True)
    starring = StarringSerializer(many=True)
    roles_dubbed = RolesDubbedSerializer(many=True)

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
                  'painters',
                  'fees_us',
                  'fees_world',
                  'image',
                  'starring',
                  'roles_dubbed',
                  ]



