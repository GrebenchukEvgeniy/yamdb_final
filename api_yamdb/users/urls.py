from django.urls import path

from .views import APICode, APISignUp, APIToken

urlpatterns = [
    path('signup/', APISignUp.as_view()),
    path('token/', APIToken.as_view()),
    path('code/', APICode.as_view()),
]
