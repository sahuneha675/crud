from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from .models import User

def index(request):
        return render(request, 'index.html')

def index2(request):
    return HttpResponse('This is the first program')

def signup(request):
    return render(request,'signup.html')


def ragistration(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        DOB = request.POST['DOB']
        password = make_password(request.POST['password'])
        if User.objects.filter(email=email).exists():
            messages.error(request,"Email alrady exists")
            return redirect('/signup/')
        elif User.objects.filter(contact=contact).exists():
            messages.error(request,"contact alrady exists")
            return redirect('/signup/')   
        else:
            User.objects.create(name=name,email=email,
                                contact=contact,DOB=DOB,
                                password=password)     
            return redirect('/login/')

def table(request):
    userdata = User.objects.all()
    return render(request,'table.html', {"userdata":userdata})

def update_view(request,uid):
    user_data = User.objects.get(id=uid)
    return render(request,'update.html', context={'data':user_data})


def update_data(request):
    if request.method == 'POST':
        name = request.POST['name']
        uid = request.POST['uid']
        email = request.POST['email']
        contact = request.POST['contact']
        DOB = request.POST['DOB']
        User.objects.filter(id=uid).update(name=name,email=email,
                            contact=contact,DOB=DOB)     
        return redirect('/table/')

def login(request):
    return render(request,'login.html')
# Create your views here.
