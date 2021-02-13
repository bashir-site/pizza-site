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

class Menu(View):
    def get(self, request):
        return render(request, 'pizza/03_menu.html')

class Blog(View):
    def get(self, request):
        return render(request, 'pizza/04_blog.html')

class Contact(View):
    def get(self, request):
        return render(request, 'pizza/05_contact.html')

class Element(View):
    def get(self, request):
        return render(request, 'pizza/06_elements.html')
