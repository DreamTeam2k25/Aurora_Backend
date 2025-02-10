from core.authentication.filters import UserFilter
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import viewsets
from core.authentication.serializers import CustomTokenObtainPairSerializer, UserSerializer

from core.authentication.models import User

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class UserViewSetList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'
    filterset_class = UserFilter 

    http_method_names = ['get', 'post', 'patch', 'put']

    ordering_fields = ['id']
    ordering = ['id']
