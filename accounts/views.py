from rest_framework import viewsets
from rest_framework.permissions import (AllowAny, IsAuthenticated)
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.permissions import IsLoggedInUserOrAdmin, IsAdminUser
from accounts.serializers import UserProfileSerializer
from .models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer

    def get_permissions(self):
        permission_class = []
        if self.action == 'create':
            permission_class = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'post':
            permission_class = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_class = [IsAdminUser]
        return [permission() for permission in permission_class]


# for accessing this we need to pass token to the header
class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'hello welcome'}
        return Response(content)
