from django.urls import path
from . import views
app_name = 'myName'
urlpatterns = [
    path('', views.index1, name="name1"),
    path('<data>/', views.index1, name="name2"),
]