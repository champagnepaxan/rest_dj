import django_filters

from .models import Category

from .models import Publication


class CategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Category
        fields = ['name']


class PublicationFilter(django_filters.FilterSet):
    content = django_filters.CharFilter(field_name='content', lookup_expr='icontains')
    category = django_filters.NumberFilter(field_name='category',
                                           lookup_expr='exact')

    class Meta:
        model = Publication
        fields = ['content', 'category', 'is_archived']