import django_filters 
from core.aurora.models import Replies

class RepliesFilter(django_filters.FilterSet):
    comment = django_filters.BaseInFilter(field_name='comment__id', lookup_expr='in')

    class Meta:
        model = Replies
        fields = ['comment']