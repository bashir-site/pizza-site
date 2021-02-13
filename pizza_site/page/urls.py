from django.urls import path

from . import views

urlpatterns = [
    path('', views.PizzaView.as_view(), name ='index'),
    path('about_us/', views.AboutUs.as_view(), name ='02_about_us'),
    path('menu/', views.Menu.as_view(), name ='03_menu'),
    path('blog/', views.Blog.as_view(), name ='04_blog'),
    path('contact/', views.Contact.as_view(), name ='05_contact'),
    path('elements/', views.Element.as_view(), name ='06_elements'),
]
