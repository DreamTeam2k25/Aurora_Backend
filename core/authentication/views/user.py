import django_filters
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import viewsets
from core.authentication.serializers import CustomTokenObtainPairSerializer, UserSerializer

from core.authentication.models import User

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class UserFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter()
    username = django_filters.CharFilter(field_name='username', lookup_expr='icontains')

    class Meta:
        model = User
        fields = ['id', 'username']

class UserViewSetList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'
    filterset_class = UserFilter 

    http_method_names = ['get']

    ordering_fields = ['id']
    ordering = ['id']