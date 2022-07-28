from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from .models import Address
from .models import BOARD

# Create your views here.
#def index(request):
#    return HttpResponse("<center><h3>안녕 장고</h3></center>")
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

from django.db.models import Q
import datetime
def list(request):
    template = loader.get_template('list.html')
    #addresses = Address.objects.all().values()
    #addresses = Address.objects.filter(name='홍길동').values()
    #addresses = Address.objects.filter(name='홍길동', addr='서울시').values()
    #addresses = Address.objects.filter(name='홍길동').values() | Address.objects.filter(addr='서울시').values()
    #addresses = Address.objects.filter(Q(name='홍길동') | Q(addr='서울시')).values()
    #addresses = Address.objects.filter(name__startswith='이')
    #addresses = Address.objects.filter(addr__contains='대')
    #addresses = Address.objects.filter(addr__icontains='구')
    #addresses = Address.objects.filter(rdate__date='2022-07-27')
    #addresses = Address.objects.filter(rdate__day='27')
    #addresses = Address.objects.filter(name__endswith='신')
    #addresses = Address.objects.filter(name__iendswith='동')
    #addresses = Address.objects.filter(name__exact='유관순')
    #addresses = Address.objects.filter(addr__iexact='BBB')
    #addresses = Address.objects.filter(name__in=['aaa'])
    #addresses = Address.objects.filter(addr__isnull=False)
    #addresses = Address.objects.filter(addr__gt='대전')
    #addresses = Address.objects.filter(name__gte='이')
    #addresses = Address.objects.filter(rdate__hour='18')
    #addresses = Address.objects.filter(addr__lt='서')
    #addresses = Address.objects.filter(name__lte='이')
    #addresses = Address.objects.filter(rdate__minute='01')
    #addresses = Address.objects.filter(rdate__month='07')
    #addresses = Address.objects.filter(rdate__quarter='3')
    #addresses = Address.objects.filter(id__range=[1,6])
    #addresses = Address.objects.filter(name__regex='AA')
    #addresses = Address.objects.filter(name__iregex='aa')
    #addresses = Address.objects.filter(rdate__second='01')
    #addresses = Address.objects.filter(addr__startswith='대')
    #addresses = Address.objects.filter(name__istartswith='A')
    #addresses = Address.objects.filter(rdate__time='14:19:01')
    #addresses = Address.objects.all().order_by('name').values()
    #addresses = Address.objects.all().order_by('-name').values()
    addresses = Address.objects.all().order_by('-name', 'addr', '-id').values()
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

from django.core.paginator import Paginator
def b_list3(request):
    template = loader.get_template('b_list.html')
    page = request.GET.get('page', 1)
    boardslist = BOARD.objects.all().order_by('-id')
    num = len(BOARD.objects.all())
    paginator = Paginator(boardslist, 3)
    page_obj = paginator.get_page(page)
    context = {
        'boards':page_obj,
        'select3':'selected',
        'pg':3,
        'num':num
    }
    return HttpResponse(template.render(context, request))
def b_list5(request):
    template = loader.get_template('b_list.html')
    page = request.GET.get('page', 1)
    boardslist = BOARD.objects.all().order_by('-id')
    num = len(BOARD.objects.all())
    paginator = Paginator(boardslist, 5)
    page_obj = paginator.get_page(page)
    context = {
        'boards':page_obj,
        'select5':'selected',
        'pg':5,
        'num':num
    }
    return HttpResponse(template.render(context, request))
def b_list10(request):
    template = loader.get_template('b_list.html')
    page = request.GET.get('page', 1)
    boardslist = BOARD.objects.all().order_by('-id')
    num = len(BOARD.objects.all())
    paginator = Paginator(boardslist, 10)
    page_obj = paginator.get_page(page)
    context = {
        'boards':page_obj,
        'select10':'selected',
        'pg':10,
        'num':num
    }
    return HttpResponse(template.render(context, request))


def b_write(request):
    template = loader.get_template('b_write.html')
    return HttpResponse(template.render({}, request))

def b_write_ok(request):
    x = request.POST['writer']
    y = request.POST['email']
    z = request.POST['subject']
    r = request.POST['content']
    nowDatetime = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
    board = BOARD(writer=x, email=y, subject=z, content=r, rdate=nowDatetime)
    board.save()
    return HttpResponseRedirect(reverse('b_list3'))

def b_content(request, id):
    template = loader.get_template('b_content.html')
    board = BOARD.objects.get(id=id)
    context = {
        'board': board,
    }
    return HttpResponse(template.render(context, request))

def b_update(request, id):
    template = loader.get_template('b_update.html')
    board = BOARD.objects.get(id=id)
    context = {
        'board': board,
    }
    return HttpResponse(template.render(context, request))

def b_update_ok(request, id):
    x = request.POST['writer']
    y = request.POST['email']
    z = request.POST['subject']
    r = request.POST['content']
    board = BOARD.objects.get(id=id)
    board.writer = x
    board.email = y
    board.subject = z
    board.content = r
    nowDatetime = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
    board.rdate = nowDatetime
    board.save()
    return HttpResponseRedirect(reverse('b_list3'))

def b_delete(request, id):
    board = BOARD.objects.get(id=id)
    board.delete()
    return HttpResponseRedirect(reverse('b_list3'))