from django.shortcuts import render,redirect
from .models import MyPost
from register.models import User
from django.contrib import messages
def index(request,email):
    desc = request.POST.get("desc")
    users = User.objects.all()
    u = None
    name = ""
    for user in users:
        if(user.email == email):
            name = user.first_name
            u = user
    if('desc' in request.POST and desc!=""):
        errors = MyPost.objects.validator(request.POST)
        if(len(errors)):
            for tag, error in errors.items():
                messages.error(request, error, extra_tags=tag)
                return redirect('/posts/'+email)
        post = MyPost.objects.create(desc=desc,user=email,name=name)
        post.save()
    myposts = MyPost.objects.all()
    context = {
        'myposts' : myposts,
        'email' : email,
        'user' : u
    }
    return render(request,'posts/index.html',context)