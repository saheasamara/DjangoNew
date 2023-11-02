from django.shortcuts import render
from .models import Order
from .forms import OrderForm


# Create your views here.

def first_page(request):
    object_list = Order.objects.all()
    form=OrderForm()
    return render(request, './index.html', {'object_list': object_list,'form':form})


def pagemsg(request):
    name = request.POST['name']
    tel = request.POST['tel']
    client = Order(order_name=name, order_tel=tel)
    client.save()
    return render(request, './addmsg.html', {'name': name, 'tel': tel})
