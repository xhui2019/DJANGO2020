from django.http import HttpResponse,Http404
from django.urls import reverse
from datetime import date
from django.shortcuts import redirect
def index1(request,data=0):
    s ="1016应用默认页面URl:%s"%(reverse("nameIndex:name1"))
    s +="<br>1016获取数据页面URL：%s"%(reverse("nameIndex:name2", args=[data]))
    return HttpResponse(s)
def showDate(request,urlData):
    d=date.today()
    s="URL路径中数据为：%s，今日当前日期是：%s"%(urlData,d)
    return HttpResponse(s)
def testCode(request):
    print(1111)
    raise Http404("没有找到对应的资源")
    # print(2222)
    # return HttpResponse("OKsfsfs洒水大大大所多所dfsfdsfsfsfs")
def getData1(request):
    s="请求上传的数据1:%s,数据2：%s"%(request.GET['name'],request.GET['age'])
    return HttpResponse(s)
def showHtml(request):
    r=HttpResponse('<h1>第一行<h1/>', content_type="text/plain;charset=GBK")
    r.write("123123132132")
    return r
def download(request):
    r = HttpResponse("文件内容", content_type="text/plain;charset=GBK")
    r["Content-Disposition"] = "attachment;filename=asd.text"
    r.write("test")
    return r
import csv
def writeCsv(request):
    r = HttpResponse(content_type="text/plain;charset=GBK")
    r["Content-Disposition"] = "attachment;filename=data.csv"
    w=csv.writer(r)
    w.writerow(["ads"])
    w.writerow(["ads","123132"])
    return r
def writeJson(request):
    r=HttpResponse(content_type="applicati123123/json;charset=utf-8")
    r.write({"name":"zzz","age":12})
    return r
def useRedirect(request):
    return redirect(getData1)
from django.template.response import TemplateResponse
def useTemplate(request):
    return TemplateResponse(request,"useTemplate.html",{"name":"zxh","age":12})

from test1016.models import test1022DB
def useModels(request):
    _name = request.GET['name']
    _age = request.GET['age']
    test1022DB.objects.create(name=_name, age=_age)
    s = '''默认数据库中表中的数据，<a href='www.baidu.com'>百度d网站</a>：<br/>
        <table>
            <tr>
                <th>id</th>
                <th>name</th>
                <th>age</th>
            </tr>'''
    for i in test1022DB.objects.all():
        s += '''<tr>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                </tr>''' % (i.id, i.name, i.age)
    return HttpResponse(s)

from django.core.paginator import Paginator
def use_paginator(request):
    _object=test1022DB.objects.all()
    _paginator = Paginator(_object, 2)
    _number = request.GET['page']
    page = _paginator.page(_number)
    str = '''数据分页显示<hr/>
            <table>
                <tr>
                <th>id</th>
                <th>name</th>
                <th>age</th>
                </tr>
            '''
    print(1111111111)
    list = page.object_list
    for i in list:
        str += '''<tr>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                </tr>''' % (i.id, i.name, i.age)
        print(22222222)
    str += '</table><hr/>'
    if page.has_previous():
        str += '''<a href='/test_j/?page=%s'>上一页</a>&nbsp&nbsp&nbsp''' % page.previous_page_number()
    str += '当前页：%s/%s &nbsp&nbsp' % (page.number, _paginator.num_pages)
    print(333333333)
    if page.has_next():
        str += '''  <a href='/test_j/?page=%s'>下一页</a>''' % page.next_page_number()
    return HttpResponse(str)
from django.views import View
class useView(View):
    new="使用基于Views类的视图11：<br>"
    form='''<form action='',method="post">
                请输入数据：<input type='text' name='data'><br>
                <input type='submit' value='提交'></form>'''
    print("111111111111111")
    def get(self,request):
        s=self.new +'请求方法：GET'+self.form
        print(2222222222222222222)
        return HttpResponse(s)
    def post(self,request):
        s=self.new+'请求方法：POST'+'上传数据为：'+request.POST['data']+self.form
        print(33333333333333333)
        return HttpResponse(s)
from datetime import datetime
from django.views.generic.detail import DetailView
from . import models
from django.views.generic import ListView


class UseDetailView(DetailView):
    model = models.test1022DB
    def get_context_data(self, **kwargs):
        content = super().get_context_data(**kwargs)
        content['now'] = datetime.now()
        return content
class UseListView(ListView):
    model = models.test1022DB

from django.template.loader import get_template
def get_time(request):
    time = datetime.today()
    t = get_template('mytemplate.html')
    html = t.render({'timenow':time})
    return HttpResponse(html)
##这行用于gitee commit测试


