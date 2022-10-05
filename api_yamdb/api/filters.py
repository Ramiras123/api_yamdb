from django_filters.rest_framework import filters

from reviews.models import Title


class TitlesFilter(filters.FilterSet):
    name = filters.CharFilter(
        field_name='name'
    )
    category = filters.CharFilter(
        field_name='category__slug'
    )
    genre = filters.CharFilter(
        field_name='genre__slug'
    )

    class Meta:
        model = Title
        fields = ['name', 'year', 'genre', 'category']
