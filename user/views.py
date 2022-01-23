from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from user.forms import CreateUserForm


class ShowUserPage(View):
    def get(self, request):
        return render(request, "user/user_main_page.html")


class CreateUser(View):
    def get(self, request):
        create_user_form = CreateUserForm()
        return render(request, "user/user_create_page.html", {'form': create_user_form})
