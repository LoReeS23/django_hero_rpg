from django.shortcuts import render
from django.views import View
from characters.models import *


class ShowMain(View):
    def get(self, request):
        pos_x = Hero.objects.all()
        pos_y = Hero.objects.all()
        return render(request, 'main.html', {'pos_x': pos_x,
                                             'pos_y': pos_y})

    def post(self, request):
        if "find_monsters" in request.POST:
            pass
        if "go_to_city" in request.POST:
            pass
        if "go_north" in request.POST:
            pass
        if "go_south" in request.POST:
            pass
        if "go_east" in request.POST:
            pass
        if "go_west" in request.POST:
            pass
