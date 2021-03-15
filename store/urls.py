from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),

	path('about_us/', views.AboutUs.as_view(), name ='02_about_us'),
    path('menu/', views.Menuu.as_view(), name ='03_menu'),
    path('blog/', views.Blog.as_view(), name ='04_blog'),
    path('contact/', views.Contact.as_view(), name ='05_contact'),
    path('elements/', views.Element.as_view(), name ='06_elements'),

]