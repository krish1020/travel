from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    if request.method == 'POST':
        a = request.POST['username']
        e = request.POST['password']
        user = auth.authenticate(username=a, password=e)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, "invalid")
            return redirect('login')

    return render(request, "login.html")



def new(request):
    if request.method=='POST':
        a = request.POST['username']
        b = request.POST['first_name']
        c = request.POST['last_name']
        d = request.POST['email']
        e = request.POST['password']
        f = request.POST['confirmpassword']
        if e==f:
            if User.objects.filter(username=a).exists():
                messages.info(request,"user name already exists")
                return redirect('new')
            elif User.objects.filter(email=d).exists():
                messages.info(request,"email already exists")
                return redirect('new')
            else:
                user = User.objects.create_user(username=a,password=e,first_name=b,last_name=c,email=d)

            user.save();
            return redirect('login')

        else:
            messages.info(request, "password does not match")
            return redirect('new')
        print('user created')
        return redirect('/')
    return render(request,"new.html")