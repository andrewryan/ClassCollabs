from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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


def results(request):
    if request.method == 'GET':
        results = User.objects.all()
        result = {}
        result['results'] = []
        for result in results:
            result['results'] += [{
                'id': result.id,
                'result': result.result
            }]
        return JsonResponse(result)


def courses(request):
    if request.method == 'GET':
        courses = course.objects.all()
        course = {}
        course['courses'] = []
        for course in courses:
            course['courses'] += [{
                'id': course.id,
                'result': course.course
            }]
        return JsonResponse(course)


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password1'))
            #login call back
            login(request,user)
            return HttpResponseRedirect('/classSearch/')

    else:
        form = RegistrationForm()
    context = {
        'title':'Registration',
        'form':form
    }
    return render(request, 'register.html', context)


def classes(request):
    context = {
        'title':'Class List',
    }
    return render(request, 'classes.html', context)


def classSearch(request):
    context = {
        'title':'Class Search',
    }
    return render(request, 'classSearch.html', context)


def discBoard(request):
    context = {
        'title':'Discussion Board',
    }
    return render(request, 'discBoard.html', context)


def message(request):
    context = {
        'title':'Messaging Center',
    }
    return render(request, 'message.html', context)
