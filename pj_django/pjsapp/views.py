from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from .models import Address

# Create your views here.
#def index(request):
#    return HttpResponse("<center><h3>안녕 장고</h3></center>")
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def list(request):
    template = loader.get_template('list.html')
    addresses = Address.objects.all().values()
    context = {
        'addresses':addresses,
    }
    return HttpResponse(template.render(context, request))

def write(request):
    template = loader.get_template('write.html')
    return HttpResponse(template.render({}, request))

from django.utils import timezone
from django.urls import reverse
def write_ok(request):
    x = request.POST['name']
    y = request.POST['addr']
    nowDatetime = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
    address = Address(name=x, addr=y, rdate=nowDatetime)
    address.save()
    return HttpResponseRedirect(reverse('list'))

def delete(request, id):
    address = Address.objects.get(id=id)
    address.delete()
    return HttpResponseRedirect(reverse('list'))

def update(request, id):
    template = loader.get_template('update.html')
    address = Address.objects.get(id=id)
    context = {
        'address': address,
    }
    return HttpResponse(template.render(context, request))

def update_ok(request, id):
    x = request.POST['name']
    y = request.POST['addr']
    address = Address.objects.get(id=id)
    address.name = x
    address.addr = y
    nowDatetime = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
    address.rdate = nowDatetime
    address.save()
    return HttpResponseRedirect(reverse('list'))
