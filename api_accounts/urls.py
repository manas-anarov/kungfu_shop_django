from rest_framework.authtoken import views as authviews
from django.urls import path
from api_accounts import views

urlpatterns = [
	path('login/', authviews.obtain_auth_token),
	path('register/', views.UserCreateAPIView.as_view(), name='restapp-registration'),
]