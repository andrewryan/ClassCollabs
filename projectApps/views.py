from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *

def index(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            submit = form.cleaned_data['comment']
            newComment = Comment(comment=submit)
            newComment.save()
            form = CommentForm()
        else:
            submit = ""
    else:
        form = CommentForm()
        submit = ""
    comments = Comment.objects.all()
    context = {
        'title':"Home",
        'content': comments,
        'form':form,
        'submit':submit
        }
    return render(request,'home.html',context)

@csrf_exempt
def comments(request):
    if request.method == 'GET':
        comments = Comment.objects.all()
        comment = {}
        comment['comments'] = []
        for comment in comments:
            comment['comments'] += [{
                'id': comment.id,
                'comment': comment.comment
            }]
        return JsonResponse(comment)
    # if self.request.is_ajax():
    #     self.object = form.save()
    #     return JsonResponse(comment)
    if request.method == 'POST':
        return HttpResponse("POST successful")
    return HttpResponse("404")


def register(request):
    if request.method == "POST":
        form = registration_form(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password1'))
            #login call back
            login(request,user)
            return HttpResponseRedirect('/')

    else:
        form = registration_form()
    context = {
        'title':'Registration',
        'form':form
    }
    return render(request, 'register.html', context)


def classes(request):
    # if request.method == "POST":
    #     form = registration_form(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         user = authenticate(
    #             username=form.cleaned_data.get('username'),
    #             password=form.cleaned_data.get('password1'))
    #         #login call back
    #         login(request,user)
    #         return HttpResponseRedirect('/')
    #
    # else:
    #     form = registration_form()
    context = {
        'title':'Class List',
        # 'form':form
    }
    return render(request, 'classes.html', context)

def classSearch(request):
    # if request.method == "POST":
    #     form = registration_form(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         user = authenticate(
    #             username=form.cleaned_data.get('username'),
    #             password=form.cleaned_data.get('password1'))
    #         #login call back
    #         login(request,user)
    #         return HttpResponseRedirect('/')
    #
    # else:
    #     form = registration_form()
    context = {
        'title':'Class Search',
        # 'form':form
    }
    return render(request, 'classSearch.html', context)

def discBoard(request):
    # if request.method == "POST":
    #     form = registration_form(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         user = authenticate(
    #             username=form.cleaned_data.get('username'),
    #             password=form.cleaned_data.get('password1'))
    #         #login call back
    #         login(request,user)
    #         return HttpResponseRedirect('/')
    #
    # else:
    #     form = registration_form()
    context = {
        'title':'Discussion Board',
        # 'form':form
    }
    return render(request, 'discBoard.html', context)

def message(request):
    # if request.method == "POST":
    #     form = registration_form(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         user = authenticate(
    #             username=form.cleaned_data.get('username'),
    #             password=form.cleaned_data.get('password1'))
    #         #login call back
    #         login(request,user)
    #         return HttpResponseRedirect('/')
    #
    # else:
    #     form = registration_form()
    context = {
        'title':'Messaging Center',
        # 'form':form
    }
    return render(request, 'message.html', context)
