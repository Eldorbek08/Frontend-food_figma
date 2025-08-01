from rest_framework import generics, permissions
from .models import CustomUser
from .serializers import UserSerializer

class SuperAdminUserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
