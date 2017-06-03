from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demo_project.views.home', name='home'),
    # url(r'^demo_project/', include('demo_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'demo_app.views.demo_index', name="home"),
    url(r'^contact$', TemplateView.as_view(template_name='contact.html'), name="contact"),
    url(r'^form$', 'demo_app.views.demo_form'),
    url(r'^form_template$', 'demo_app.views.demo_form_with_template'),
    url(r'^form_inline$', 'demo_app.views.demo_form_inline'),
    url(r'^formset$', 'demo_app.views.demo_formset', {}, "formset"),
    url(r'^tabs$', 'demo_app.views.demo_tabs', {}, "tabs"),
    url(r'^pagination$', 'demo_app.views.demo_pagination', {}, "pagination"),
    url(r'^widgets$', 'demo_app.views.demo_widgets', {}, "widgets"),
    url(r'^buttons$', 'demo_app.views.demo_buttons', {}, "buttons"),
    url(r'^search$', 'demo_app.views.demo_search', {}, "search"),
    url(r'^ding$', "demo_app.views.demo_ding"),
    url(r'^deltopic$', TemplateView.as_view(template_name='deltopic.html'), name="deltopic"),
    url(r'^compare$',"demo_app.views.demo_compare"),
    url(r'^edituser$',"demo_app.views.demo_edituser"),
    url(r'^submittxt$','demo_app.views.demo_submittxt', {}, "search"),
    url(r'^login$','demo_app.views.demo_login',name='login'),
    url(r'^regist$','demo_app.views.demo_regist',name='regist'),
    url(r'^login$','demo_app.views.demo_logout',name='logout'),
    url(r'^registcenter$','demo_app.views.demo_registcenter',name='registcenter'),
    url(r'^manage$', TemplateView.as_view(template_name='manage.html'), name="manage"),
    url(r'^managelogin$', 'demo_app.views.manage_login',name='managelogin'),
    url(r'^managefruit$', 'demo_app.views.fruit_manage',name='managefruit'),
    )
