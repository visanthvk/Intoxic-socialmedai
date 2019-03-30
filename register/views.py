from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User

def index(request):
    return render(request, 'register/index.html')

def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error, extra_tags=tag)
        return redirect('/register/')   

    hashed_password = request.POST['password']
    user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], password=hashed_password, email=request.POST['email'],age=request.POST['age'],gender=request.POST['gender'])
    user.save()
    request.session['id'] = user.id
    return redirect('/posts/'+request.POST['email'])

def login(request):
    if (User.objects.filter(email=request.POST['login_email']).exists()):
        user = User.objects.filter(email=request.POST['login_email'])[0]
        if (request.POST['login_password']):
            request.session['id'] = user.id
            return redirect('/posts/'+request.POST['login_email'])
    return redirect('/register/')