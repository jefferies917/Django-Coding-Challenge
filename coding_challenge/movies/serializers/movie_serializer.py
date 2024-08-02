from rest_framework import serializers
from movies.models import Movie, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["name", "rating"]


class MovieSerializer(serializers.ModelSerializer):
    runtime_formatted = serializers.SerializerMethodField()
    avg_rating = serializers.SerializerMethodField()
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "runtime",
            "runtime_formatted",
            "release_date",
            "avg_rating",
            "reviews",
        ]

    def get_runtime_formatted(self, obj):
        hours = obj.runtime // 60
        minutes = obj.runtime % 60
        return f"{hours}:{minutes:02d}"

    def get_avg_rating(self, obj):
        if obj.reviews.exists():
            return round(
                obj.reviews.aggregate(avg_rating=models.Avg("rating"))["avg_rating"], 2
            )
        return 0.0


class MovieDetailSerializer(MovieSerializer):
    reviews = ReviewSerializer(many=True)

    class Meta(MovieSerializer.Meta):
        fields = MovieSerializer.Meta.fields
