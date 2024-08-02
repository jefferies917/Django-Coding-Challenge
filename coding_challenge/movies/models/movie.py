from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100, unique=True)
    runtime = models.PositiveIntegerField()
    release_date = models.DateField()

    def __str__(self):
        return self.title


class Review(models.Model):
    movie = models.ForeignKey(Movie, related_name="reviews", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    rating = models.PositiveIntegerField(
        choices=[(i, i) for i in range(1, 6)]
    )  # 1 to 5 stars

    def __str__(self):
        return f"{self.name} - {self.rating} Stars"
