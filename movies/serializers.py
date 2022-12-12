from rest_framework import serializers

from movies.models import Movie, Rating


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id',
                  'title',
                  'description',
                  'subtitles',
                  'year',
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
                  'year',
                  'country',
                  'genre',
                  'fees_us',
                  'fees_world',
                  'image',
                  ]


class CreateRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['star',
                  'movie'
                  ]

    def create(self, validated_data):
        rating = Rating.objects.update_or_create(
            ip=validated_data.get('ip', None),
            movie=validated_data.get('movie', None),
            defaults={'star': validated_data.get('star')}
        )

        return rating