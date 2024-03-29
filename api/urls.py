from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('register/',views.RegisterAPIView.as_view()),
    path('login/',obtain_auth_token),
    path('islogged/',views.CheckIfLoggedIn.as_view())
]