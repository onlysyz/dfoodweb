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
from .forms import TestForm, TestModelForm, TestInlineForm, WidgetsForm, FormSetInlineForm
import json  
from django.http.response import HttpResponse

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
    user_list=models.user.objects.get(username='测试用户1')
    layout = request.GET.get('layout')
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


def demo_formset(request):
    from demo_app import models
    cache.set('ding',131,settings.NEVER_REDIS_TIMEOUT)
    news_list=models.News.objects.all()
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
    }))

@csrf_exempt
def demo_search(request):
    from demo_app import models
    foodname=request.GET.get('food')
    food_list=models.helfruit.objects.get(rfoodname=foodname)
    layout = request.GET.get('layout', 'vertical')
    form = WidgetsForm()
    ding=cache.get('ding');
    return render_to_response('search.html', RequestContext(request, {
        'form': form,
        'layout': layout,
        'food_list':food_list,
        'ding':ding,
    }))

def demo_compare(request):
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
        'formset': formset,
        'layout': layout,
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
    lines = []
    for i in range(10000):
        lines.append(u'Line %s' % (i + 1))
    paginator = Paginator(lines, 10)
    page = request.GET.get('page')
    try:
        show_lines = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        show_lines = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        show_lines = paginator.page(paginator.num_pages)
    return render_to_response('pagination.html', RequestContext(request, {
        'lines': show_lines,
    }))


def demo_widgets(request):
    layout = request.GET.get('layout', 'vertical')
    form = WidgetsForm()
    return render_to_response('form.html', RequestContext(request, {
        'form': form,
        'layout': layout,
    }))
