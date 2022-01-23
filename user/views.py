from django.shortcuts import render
from django.views import View


class ShowUserPage(View):
    def get(self, request):
        return render(request, "user_page.html")

    def post(self, request):
        pass
