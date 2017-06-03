# -*- coding:utf8 -*-
from django.contrib import messages
from django.forms.formsets import formset_factory
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.conf import settings
from django.core.cache import cache
from bootstrap_toolkit.widgets import BootstrapUneditableInput
from django.views.decorators.csrf import csrf_exempt 
from .forms import TestForm, TestModelForm, TestInlineForm, WidgetsForm, FormSetInlineForm,LoginForm
import json  
from django.http.response import HttpResponse
import csv
import codecs

# class UserForm(forms.Form):
#     username=forms.char
def demo_index(request):
    from demo_app import models
    return render_to_response('index.html', RequestContext(request, {
        
    }))

def manage_login(request):
    from demo_app import models
    if request.method=="POST":
        f=LoginForm(request.POST)
        if f.is_valid():
            user=f.cleaned_data["username"]
            pwd=f.cleaned_data["password"]
            result=models.userinfo.objects.filter(user_exact=user,pwd_exact=pwd)
            if  result:
                models.userinfo.objects.filter(user_exact=user).update(status=1)
                request.session["user"]=user
                return render_to_response('backendindex.html',RequestContext(request,{"error":f.errors,"form":f}))
            else:
                f.errors["password"]="密码错误"
                return render_to_response('manage.html',RequestContext(request,{"error":f.errors,"form":f}))
        else:
            return render_to_response('manage.html',RequestContext(request,{"error":f.errors,"form":f}))

def fruit_manage(request):
    from demo_app import models
    fruit_list=models.helfruit.objects.all()
    return render_to_response('fruitmanage.html', RequestContext(request, {
        'fruit_list':fruit_list,
    }))

def demo_form_with_template(request):
    layout = request.GET.get('layout')
    if not layout:
        layout = 'vertical'
    if request.method == 'POST':
        form = TestForm(request.POST)
        form.is_valid()
    else:
        form = TestForm()
    modelform = TestModelForm()
    return render_to_response('form_using_template.html', RequestContext(request, {
        'form': form,
        'layout': layout,
    }))

def demo_form(request):
    from demo_app import models
    value = request.COOKIES["history"]
    user_list=models.user.objects.get(username='测试用户1')
    layout = request.GET.get('layout')
    list_test=value.split("*")
    food_new_list=models.helfruit.objects.order_by('id')[:6]
    need_list=[None]*6
    food_dict={}
    l=0
    for i in food_new_list:
        food_dict['name']=i.rfoodname
        food_dict['img']=i.rfoodname+".jpg"
        food_dict['url']='/search?food='+i.rfoodname
        need_list[l]=food_dict
        food_dict={}
        l=l+1
    if not layout:
        layout = 'vertical'
    if request.method == 'POST':
        form = TestForm(request.POST)
        form.is_valid()
    else:
        form = TestForm()
    form.fields['title'].widget = BootstrapUneditableInput()
    return render_to_response('form.html', RequestContext(request, {
        'form': form,
        'layout': layout,
        'user_list': user_list,
        'value':value,
        'food_new_list':food_new_list,
        'need_list':need_list,
    }))

def demo_edituser(request):
    from demo_app import models
    user_list=models.user.objects.get(username='测试用户1')
    return render_to_response('edituser.html', RequestContext(request, {
        'user_list': user_list,
    }))


def demo_form_inline(request):
    layout = request.GET.get('layout', '')
    if layout != 'search':
        layout = 'inline'
    form = TestInlineForm()
    return render_to_response('form_inline.html', RequestContext(request, {
        'form': form,
        'layout': layout,
    }))

def demo_logout(request):
    return render_to_response('login.html', RequestContext(request, {
        
    }))
def demo_login(request):
    return render_to_response('login.html', RequestContext(request, {
        
    }))
def demo_regist(request):
    return render_to_response('regist.html', RequestContext(request, {
        
    }))

def demo_registcenter(request):
    from demo_app import models
    email=request.POST.get('email')
    name=request.POST.get('name')
    pwd=request.POST.get('pwd')
    age=request.POST.get('age')
    hobby=request.POST.get('hobby')
    taste=request.POST.get('taste')
    title=request.POST.get('title')
    models.user.objects.create(id=2,email=email,username=name,password=pwd,sex=1,age=age,hobby=hobby,taste=taste,title=title,collect=1)
    return render_to_response('index.html', RequestContext(request, {
        
    }))

def demo_formset(request):
    from demo_app import models
    cache.set('ding',131,settings.NEVER_REDIS_TIMEOUT)
    news_list=models.News.objects.all()
    food_list=models.helfruit.objects.all().order_by('rheat')
    list1=food_list[:9]
    list2=[None]*9
    l=0
    for i in list1:
        name=i.rfoodname+".jpg"
        list2[l]=name
        l=l+1
    layout = request.GET.get('layout')
    if not layout:
        layout = 'inline'
    DemoFormSet = formset_factory(FormSetInlineForm)
    if request.method == 'POST':
        formset = DemoFormSet(request.POST, request.FILES)
        formset.is_valid()
    else:
        formset = DemoFormSet()
    return render_to_response('formset.html', RequestContext(request, {
        'formset': formset,
        'layout': layout,
        'news_list':news_list,
        'list2':list2,
    }))

@csrf_exempt
def demo_search(request):
    from demo_app import models
    foodname=request.GET.get('food')
    food_list=models.helfruit.objects.get(rfoodname=foodname)
    imageplace=food_list.rfoodname+".jpg"
    layout = request.GET.get('layout', 'vertical')
    food_new_list=models.helfruit.objects.order_by('id')[:6]
    compare_list=[None]*6
    l=0
    for i in food_new_list:
        compare_list[l]=i.rfoodname+".jpg"
        l=l+1
    form = WidgetsForm()
    ding=cache.get('ding');
    return render_to_response('search.html', RequestContext(request, {
        'form': form,
        'layout': layout,
        'food_list':food_list,
        'ding':ding,
        'imageplace':imageplace,
        'compare_list':compare_list,
        'food_new_list':food_new_list,
    }))

def demo_compare(request):
    from demo_app import models
    fruit1=request.GET.get('fruit1')
    fruit2=request.GET.get('fruit2')
    fruit1img=fruit1+".jpg"
    fruit2img=fruit2+".jpg"
    food_list=models.helfruit.objects.get(rfoodname=fruit1)
    food_list2=models.helfruit.objects.get(rfoodname=fruit2)
    heat1=test1(float(food_list.rheat),float(food_list2.rheat))[0]
    heat2=test1(float(food_list.rheat),float(food_list2.rheat))[1]
    fat1=test1(float(food_list.rfat),float(food_list2.rfat))[0]
    fat2=test1(float(food_list.rfat),float(food_list2.rfat))[1]
    cellulose1=test1(float(food_list.rcellulose),float(food_list2.rcellulose))[0]
    cellulose2=test1(float(food_list.rcellulose),float(food_list2.rcellulose))[1]
    co21=test1(float(food_list.rco2),float(food_list2.rco2))[0]
    co22=test1(float(food_list.rco2),float(food_list2.rco2))[1]
    protein1=test1(float(food_list.rprotein),float(food_list2.rprotein))[0]
    protein2=test1(float(food_list.rprotein),float(food_list2.rprotein))[1]
    name=fruit1+"+"+fruit2+".csv"
    csvfile = file('E:\django\demo_project\static\csv/%s'%name, 'wb')
    csvfile.write(codecs.BOM_UTF8)
    writer = csv.writer(csvfile)
    writer.writerow(['company', 'type1','type2','type3','type4','type5'])

    fruit1de=fruit1.encode('utf8')
    fruit2de=fruit2.encode('utf8')
    data = [
        (fruit1de,heat1,fat1,cellulose1,co21,protein1),
        (fruit2de,heat2,fat2,cellulose2,co22,protein2)
    ]
    writer.writerows(data)

    csvfile.close()
    food_new_list=models.helfruit.objects.order_by('id')[:6]
    compare_list=[None]*6
    l=0
    for i in food_new_list:
        compare_list[l]=i.rfoodname+".jpg"
        l=l+1
    layout = request.GET.get('layout')
    if not layout:
        layout = 'inline'
    DemoFormSet = formset_factory(FormSetInlineForm)
    if request.method == 'POST':
        formset = DemoFormSet(request.POST, request.FILES)
        formset.is_valid()
    else:
        formset = DemoFormSet()
    return render_to_response('compare.html', RequestContext(request, {
        'fruit1':fruit1,
        'fruit2':fruit2,
        'formset': formset,
        'layout': layout,
        'fruit1img':fruit1img,
        'fruit2img':fruit2img,
        'food_list':food_list,
        'food_list2':food_list2,
        'compare_list':compare_list,
        'food_new_list':food_new_list,
        'name':name,
    }))

@csrf_exempt
def demo_ding(request):
    ding=request.POST.get('num')
    ding=int(ding)+1
    cache.set('ding',ding,settings.NEVER_REDIS_TIMEOUT)
    return HttpResponse(json.dumps({"msg":ding}))
    
def demo_tabs(request):
    layout = request.GET.get('layout')
    if not layout:
        layout = 'tabs'
    tabs = [
        {
            'link': "#",
            'title': 'Tab 1',
            },
        {
            'link': "#",
            'title': 'Tab 2',
            }
    ]
    return render_to_response('tabs.html', RequestContext(request, {
        'tabs': tabs,
        'layout': layout,
    }))


def demo_pagination(request):
    from demo_app import models
    food_list=models.food.objects.order_by('id')
    food_list1=food_list[:10]
    return render_to_response('pagination.html', RequestContext(request, {
        'food_list': food_list,
        'food_list1': food_list1,
    }))

def demo_buttons(request):
    from demo_app import models
    news_list=models.tiezi.objects.all()
    layout = request.GET.get('layout')
    return render_to_response('buttons.html', RequestContext(request, {
        'layout': layout,
        'news_list':news_list,
    }))

def demo_widgets(request):
    layout = request.GET.get('layout', 'vertical')
    form = WidgetsForm()
    return render_to_response('form.html', RequestContext(request, {
        'form': form,
        'layout': layout,
    }))

def demo_submittxt(request):
    from demo_app import models
    newtitle = request.POST.get('title')
    models.tiezi.objects.create(title=newtitle)
    news_list=models.tiezi.objects.all()
    layout = request.GET.get('layout')
    return render_to_response('buttons.html', RequestContext(request, {
        'news_list': news_list,
        'layout': layout,
    }))

def test1(a,b):
    a1=a
    b1=b
    if a1<b1:
        zz=a1
        a1=b1
        b1=zz
    if b1<1:
        if a1/b1>5:
            a1=5
            b1=1
        else:
            a1=a1/b
            b1=1
    else:
        while(a1/b1>=5):
            a1=a1/5
        while b1>5:
            b1=b1/5
            a1=a1/5
    if a1>5:
        a1=a1/5
        b1=b1/5
        if b1<1:
            b1=1
    if a>b:
        a=a1
        b=b1
    else:
        a=b1
        b=a1
    a=int(a)*2
    b=int(b)*2
    list1=[None]*2
    list1[0]=a
    list1[1]=b
    return list1