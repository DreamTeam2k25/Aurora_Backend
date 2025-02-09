import django_filters
from core.authentication.models import User

class UserFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter()
    username = django_filters.CharFilter(field_name='username', lookup_expr='icontains')

    class Meta:
        model = User
        fields = ['id', 'username']