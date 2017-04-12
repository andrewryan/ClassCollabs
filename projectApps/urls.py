from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'register',views.register, name='register'),
    url(r'classes',views.classes, name='classes'),
    url(r'classSearch',views.classSearch, name='classSearch'),
    url(r'discBoard',views.discBoard, name='discBoard'),
    url(r'message',views.message, name='message'),
]
