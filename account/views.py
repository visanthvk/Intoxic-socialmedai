from django.shortcuts import render,redirect
from register.models import User
from posts.models import MyPost
def index(request,email):
    users = User.objects.all()
    user = None
    posts = MyPost.objects.all()
    for i in users:
        if(i.email == email):
            user = i    
    context = {
        'email':email,
        'user' : user,
        'posts' : posts
    }
    return render(request, 'account/index.html',context)

def update(request,email):
    users = User.objects.all()
    u = users.filter(email=email).update(first_name=request.POST.get('f_name'),last_name=request.POST.get('l_name'),age=request.POST.get('age'),gender=request.POST.get('gender'))
    posts = MyPost.objects.all()
    v = posts.filter(user=email).update(name=request.POST.get('f_name'))
    return redirect('/account/'+email)
