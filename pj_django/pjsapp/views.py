from re import template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader
from .models import Address
from .models import BOARD
from .models import MEMBER

# Create your views here.
#def index(request):
#    return HttpResponse("<center><h3>안녕 장고</h3></center>")

def index(request): 
    template = loader.get_template('index.html')
    user_id = request.session.get('login_ok_user')
    print("user_id:", user_id)
    if user_id:
        context = {'id':True}
        print('1')
        return HttpResponse(template.render(context, request))
    else:
        context = {'id':False}
        print('2')
        return HttpResponse(template.render(context, request))

'''
def index(request): #선생님코드
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))
'''

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


def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render({}, request))

def login_ok(request):
    template = loader.get_template('login_ok.html')
    if request.method == "POST":
        useremail = request.POST['email']
        userpwd = request.POST['pwd']
        
        try:
            user = MEMBER.objects.get(email=useremail)
            if user.email == useremail:
                if user.pwd == userpwd:
                    request.session['login_ok_user'] = user.id
                    result = 2
                    context = {
                        'result': result,
                    }
                    return HttpResponse(template.render(context, request))
                else:
                    result = 1
                    context = {
                        'result' : result,
                    }
                    return HttpResponse(template.render(context, request))                             
        except:
            result = 0
            context = {
                    'result' : result,
            }
            return HttpResponse(template.render(context, request))

def logout(request):
    if request.session.get('login_ok_user'):
        del(request.session['login_ok_user'])
    return HttpResponseRedirect(reverse('index'))

'''
def login(request): #선생님 코드
    #template = loader.get_template('login.html') #방법1
    #return HttpResponse(template.render({}, request))
    return render(request, 'login.html') #방법2

from .models import MEMBER

def login_ok(request):
    #email = request.POST['email'] #방법1
    #pwd = request.POST['pwd'] #방법1
    email = request.POST.get('email', None)
    pwd = request.POST.get('pwd', None)
    print("email", email, "pwd", pwd)
    
    try:
        member = MEMBER.objects.get(email=email)
    except MEMBER.DoesNotExist:
        member = None
    print(member)
    
    if member != None:
        print("해당 email회원 존재함")
        if member.pwd == pwd:
            print("비밀번호 일치")
            result = 2
            
            print("member.email", member.email)#방법1
            request.session['login_ok_user'] = member.email #방법1
            
            #session_id = request.session.session_key #방법2
            #print("session_id", session_id) #방법2
            #request.session['login_ok_user'] = session_id #방법2
        else:
            print("비밀번호 틀림")
            result = 1 
    else:
        print("해당 email회원 존재하지 않음")
        result = 0
    
    template = loader.get_template('login_ok.html')
    context = {
        'result' : result,
    }
    return HttpResponse(template.render(context, request))

def logout(request):
			if request.session.get('login_ok_user'):
				del request.session['login_ok_user']
				#request.session.clear() # 서버측의 해당 user의 session방을 초기화
				#request.session.flush() # 서버측의 해당 user의 session방을 삭제
			return redirect("../")
'''