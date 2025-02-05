import django_filters 
from core.aurora.models import Comments

class CommentsFilter(django_filters.FilterSet):
    post = django_filters.BaseInFilter(field_name='post__id', lookup_expr='in')

    class Meta:
        model = Comments
        fields = ['post']