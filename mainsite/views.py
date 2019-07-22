from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.models import User
from mainsite import models
# Create your views here.


def login(request):
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            login_name = request.POST['username'].strip()
            login_password = request.POST['password']
            user = authenticate(username=login_name, password=login_password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    messages.add_message(request, messages.SUCCESS, '成功登入了')
                    return redirect('/')
                else:
                    messages.add_message(request, messages.WARNING, '帳號未啟用')

            else:
                messages.add_message(request, messages.WARNING, '登入失敗')
        else:
            messages.add_message(request, messages.INFO, '請檢察欄位內容')
    else:
        login_form = forms.LoginForm()
    return render(request, 'login.html', locals())


def homepage(request, pid=None, del_pass=None):
    if request.user.is_authenticated:
        username = request.user.username
        user_all = request.user
    messages.get_messages(request)
    news = models.Post.objects.all().order_by('-id')
    now = datetime.now()
    user = User.objects.all()
    return render(request, 'homepage.html', locals())


def logout(request):
    auth.logout(request)
    messages.add_message(request, messages.INFO, '成功登出惹')
    return redirect('/')


def register(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            User.objects.create_user(username=username, password=password, email=email)
            # return redirect('/')
            return render(request, 'pagejump.html', locals())
        else:
            return render(request, 'register.html', locals())
    else:
        form = forms.RegisterForm()
        return render(request, 'register.html', locals())


def post(request):
    if request.user.is_authenticated:
        userid = request.user.id
        username = request.user.username
    if request.method == 'POST':
        form = forms.PostForm(request.POST)
        if form.is_valid():
            title = request.POST.get('title')
            post = request.POST.get('post')
            models.Post.objects.create(user_id=userid, name=username, title=title, post=post)
            return redirect('/')
        else:
            return render(request, 'post.html', locals())
    else:
        form = forms.PostForm()
        return render(request, 'post.html', locals())

