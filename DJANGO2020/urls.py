"""DJANGO2020 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.urls import re_path
from test1016 import views
from django.conf.urls import url

urlpatterns = [
    # re_path(r'^[a-zA-Z]+$', views.CharUrl),
    # path("test1014app/", include('test1014.urls')),
    # re_path(r'^\d{3,}$', views.NumberUrl),
    # path('test', views.index),
    # path('admin/', admin.site.urls),
    # path('getdata/<Data>/', views.getData),
    # path('getdata/<Data1>/<Data2>/', views.getData2),
    # path('changeData/<slug:Data>/', views.changeData),
    # path('exdata/<Data>',views.getExdata,{"name":"zouxiaohui","age":18,"addr":"sz"}),
    # path('geturl/url/',views.getUrl1, name="url1"),
    # path('geturl/url2/<data>', views.getUrl2, name="url2"),
    # path('geturl/url3/<Data001>', views.getUrl3, name="url3"),
    # path('geturl/url4/',views.getView),
    # path('geturl/url5/<path:data>',views.getUrl5,name='urlTemplates'),
    # path('usename3/', include(('test1016.urls', 'myName'), namespace="nameIndex")),
    # path('usename4/', include(('test1016.urls', 'myName'), namespace="nameIndex")),
    path('test_a/<urlData>', views.showDate),
    path('test_ab/',views.testCode),
    path('get/',views.getData1),
    path('test_c/',views.showHtml),
    path('test_d/', views.download),
    path('test_e/', views.writeCsv),
    path('test_f/',views.writeJson),
    path('test_g/', views.useRedirect),
    path('test_h/', views.useTemplate),
    path('test_i/', views.useModels),
    path('test_j/', views.use_paginator),
    path('test_k/',views.useView.as_view()),
    path('test_l/', views.UseListView.as_view()),
    path('test_m/<int:pk>', views.UseDetailView.as_view()),
    path('test_n',views.get_time),
    path('test_o',views.use_template_b),
    path('test_p/',views.use_for),
    path('test_q/', views.use_extend),
    url('getdata/',views.getdata),
    url('test_r/',views.use_form),
    url('test_s/', views.xuan_ruan),
]
