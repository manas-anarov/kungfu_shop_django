

from .serializers import UserCreateSerializer

from rest_framework.generics import (CreateAPIView)

from django.contrib.auth import get_user_model
User = get_user_model()





from rest_framework.response import Response

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication



class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer
	queryset = User.objects.all()