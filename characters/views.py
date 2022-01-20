from django.shortcuts import render
from django.views import View
from models import *


class ShowMain(View):
    def get(self, request):
        return render(request, 'main.html', {'current_pos': CURRENT_POSITION})

    def post(self, request):
        pass
