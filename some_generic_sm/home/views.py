from django.shortcuts import render, redirect
from django.views import View


class HomeView(View):
    template_name = 'home/home.html'

    def get(self, request):
        return render(request, self.template_name)