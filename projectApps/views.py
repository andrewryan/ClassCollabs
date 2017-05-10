from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from Project import settings

from .models import *
from .forms import *


def index(request):
    context = {
        'title':"Home",
        }
    return render(request,'home.html',context)


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        HttpResponseRedirect('/classes/')
    else:
        return HttpResponse("Invalid login credentials")


def logout_view(request):
    logout(request)
    return HttpResponse("You have been successfully logged out")


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password1'))
            #log the user in
            login(request,user)
            return HttpResponseRedirect('/classSearch/')

    else:
        form = RegistrationForm()
    context = {
        'title':'Registration',
        'form':form
    }
    return render(request, 'register.html', context)


@login_required
def classes(request):
    availClasses = Course.objects.all()
    context = {
        'class_list':availClasses,
        'title':'Class List',
    }
    return render(request, 'classes.html', context)

@login_required
def classSearch(request):
    availClasses = Course.objects.all()
    context = {
        'class_list':availClasses,
        'title':'Class Search',
    }
    return render(request, 'classSearch.html', context)

@login_required
def discBoard(request):
    users = User.objects.select_related('logged_in_user')
    for user in users:
        if hasattr(user, 'logged_in_user'):
            user.status = 'Online'
        else:
            ''
    context = {
        'title':'Discussion Board',
        'users':users,
    }
    return render(request, 'discBoard.html', context)


@login_required
def message(request):
    context = {
        'title':'Messaging Center',
    }
    return render(request, 'message.html', context)

@login_required
def home(request):
    context = {
        'title':'Home',
    }
    return render(request, 'home.html', context)
