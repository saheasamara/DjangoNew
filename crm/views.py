from django.shortcuts import render
from .models import Order


# Create your views here.

def first_page(request):
    object_list = Order.objects.all()
    return render(request, './index.html', {'object_list': object_list})


def pagemsg(request):
    name = request.GET['name']
    tel = request.GET['tel']
    client = Order(order_name=name, order_tel=tel)
    client.save()
    return render(request, './addmsg.html', {'name': name, 'tel': tel})
