from django_filters import FilterSet
from .models import New


class NewFilter(FilterSet):
    class Meta:
        model = New
        fields = {
            'name': ['icontains'],
            'author': ['icontains'],
            'datetime': ['gt'],
        }