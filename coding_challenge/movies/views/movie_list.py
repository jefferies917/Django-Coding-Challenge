from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.filters import OrderingFilter
from movies.models import Movie, Review
from movies.serializers import MovieSerializer, MovieDetailSerializer
from django_filters import rest_framework as filters


class MovieListView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["runtime"]
    ordering_fields = ["runtime"]

    def get_queryset(self):
        queryset = super().get_queryset()
        min_runtime = self.request.query_params.get("min_runtime", None)
        max_runtime = self.request.query_params.get("max_runtime", None)

        if min_runtime is not None:
            queryset = queryset.filter(runtime__gte=int(min_runtime))
        if max_runtime is not None:
            queryset = queryset.filter(runtime__lte=int(max_runtime))

        return queryset


class MovieDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer
