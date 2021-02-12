from django.urls import path

from . import views

urlpatterns = [
    path('', views.PizzaView.as_view()),
    path('02_about_us/', views.AboutUs.as_view()),
]
