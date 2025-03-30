from rest_framework import serializers
from movies.models import Movie
from genres.serializers import GenreSerializer
from actors.serializers import ActorsSerializer
from django.db.models import Avg


class MovieModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

    # validando serializer, validate_(nome do campo)
    def validate_release_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError(
                'A data de lançamento não pode ser menor que 1990')
        return value


class MovieListDetailSerializer(serializers.ModelSerializer):
    gerre = GenreSerializer(many=True)
    actors = ActorsSerializer()
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = [
            'id',
            'title',
            'genre',
            'actors',
            'release_date',
            'rate',
            'resume'
        ]

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)

    # Calcula a média das estrelas
        # reviews = obj.reviews.all()

        # #verifica se há alguma review
        # if reviews:
        #     sum_reviews = 0

        #      #incrementa as estrelas recebidas
        #     for review in reviews:
        #         sum_reviews += review.stars

        #     reviews_count= reviews.count()

        #     return round(sum_reviews / reviews_count, 1)

        # return None
