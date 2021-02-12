from django.shortcuts import render
from django.views.generic.base import View

from .models import Pizza

class PizzaView(View):
    def get(self, request):
        pizza = Pizza.objects.all()
        return render(request, 'pizza/index.html', { 'pizza_list': pizza })

class AboutUs(View):
    def get(self, request):
        return render(request, 'pizza/02_about_us.html')
