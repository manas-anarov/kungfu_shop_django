from django import forms


from django.contrib.auth.forms import UserCreationForm
# from myaccount.models import ExtendetUser
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
User = get_user_model()
class RegisterForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('username', 'password1', 'password2')