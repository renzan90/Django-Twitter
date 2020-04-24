from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect, Http404
from TClone.models import Tweet, Profile
from django.contrib.auth.models import User
from TClone.forms import UserCreateForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.template import loader
from TClone.forms import LoginForm
from django.views.decorators.cache import cache_control
from TClone.forms import TweetForm
from .models import *
from .forms import *



def index(request):
    template = loader.get_template('TCloneTemplates/index.html')
    return HttpResponse(template.render())

@csrf_protect
def signup(request):
    if request.method=="POST":
        form=UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            email=form.cleaned_data.get('email')
            first_name=form.cleaned_data.get('firstname')
            last_name=form.cleaned_data.get('lastname')
            password1=form.cleaned_data.get('password1')
            password2=form.cleaned_data.get('password2')

            if password1==password2:
                if User.objects.filter(username=username).exists():
                    print('Username already taken')
                elif User.objects.filter(email=email).exists():
                    print('Email already taken')
                else:
                    user=User.objects.create(username=username, email=email, first_name=first_name, last_name=last_name, password=password1)
                    user.save()
                    login(request, user)
                    return HttpResponseRedirect('TCloneTemplates/homepage.html')
            else:        
                print('passwords not matching')
                return redirect('/')
    else:
        form = UserCreateForm()
    return render(request, 'TCloneTemplates/signup.html', {'form':form})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@csrf_protect
def authentication(request):
    
    if request.method=='POST':
        form=AuthenticationForm(request, request.POST)
        if form.is_valid():
            #form.save()
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username, password=password)
            login(request, user)
            return redirect('/home/')
        else:
            print('failure!!')
    else:
        form=AuthenticationForm()
    return render(request, 'TCloneTemplates/login.html', {'form':form})

@csrf_protect
@login_required
def tweeter(request):
    tweets=Tweet.objects.all()
    form=TweetForm()
    if request.method=='POST':
        form=TweetForm(request.POST)
        print(form.errors)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=request.user
            post.save()
        return redirect('/home/')   
    else:
        form=TweetForm()
    context={"form":form, "tweets":tweets}
    return render(request, 'TCloneTemplates/homepage.html', context)
  
@csrf_protect
def logouter(request):
    logout(request)
    return HttpResponse(render(request,'TCloneTemplates/index.html'))








