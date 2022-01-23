from django.urls import path, include
from user.views import *

urlpatterns = [
    path('', ShowUserPage.as_view()),
    path('create/', CreateUser.as_view())
]