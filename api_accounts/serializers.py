from rest_framework import serializers

from django.contrib.auth import get_user_model
from rest_framework.serializers import (
      ModelSerializer,
)



from django.contrib.auth import get_user_model
User = get_user_model()


class UserCreateSerializer(ModelSerializer):
   password = serializers.CharField(
      min_length=4,
      write_only=True,
      required=True,
      style={'input_type': 'password'}
   )
   email = serializers.EmailField(required=False,)

   class Meta:
      model = User
      fields = [
         'id',
         'username',
         'password',
         'email',
      ]
   extra_kwargs = {"password":
               {"write_only":True},
               "id":
               {"read_only":True}
               }

   def validate(self, data):
      return data


   def create(self, validated_data):
      username = validated_data['username']
      password = validated_data['password']
      email = validated_data['email']
      user_obj = User(
         username = username,
         email = email,
      )
      user_obj.set_password(password)
      user_obj.save()
      return user_obj