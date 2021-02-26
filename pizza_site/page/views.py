from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.http import JsonResponse
import json
import datetime

from .models import *
from .utils import cookieCart, cartData, guestOrder

class PizzaView(View):
    def get(self, request):
        pizza = Pizza.objects.all()
        category = Category.objects.all()
        menu = Menu.objects.all()
        return render(request, 'pizza/index.html', { 'pizza_list': pizza , 'category_list': category, 'menu_list': menu ,})


class AboutUs(View):
    def get(self, request):
        return render(request, 'pizza/02_about_us.html')

class Menuu(View):
    def get(self, request):
        return render(request, 'pizza/03_menu.html',)

class Blog(View):
    def get(self, request):
        return render(request, 'pizza/04_blog.html')

class Contact(View):
    def get(self, request):
        return render(request, 'pizza/05_contact.html')

class Element(View):
    def get(self, request):
        return render(request, 'pizza/06_elements.html')

def cart(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'cart.html', context)

def checkout(request):
	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	pizzaId = data['pizzaId']
	action = data['action']
	print('Action:', action)
	print('Pizza:', pizzaId)

	customer = request.user.customer
	pizza = Pizza.objects.get(id=pizzaId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, pizza=pizza)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
		)

	return JsonResponse('Payment submitted..', safe=False)