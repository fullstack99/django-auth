from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from .models import User

def index(request):
    return render(request, 'register/index.html')

def register(request):
    if request.method == "POST":
        errors = User.objects.validator(request.POST)
        if len(errors):
            for tag, error in errors.items():
                messages.error(request, error, extra_tags=tag)
                return redirect('/register')

        hashed_password = bcrypt.hashpw(request.POST['password'].encode('utf-8'), bcrypt.gensalt())
        user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], password=hashed_password, email=request.POST['email'])
        user.save()
        request.session['id'] = user.id
        return redirect('/success')
    else:
        return render(request, 'register/signup.html')

def login(request):
    if request.method == "POST":
        if (User.objects.filter(email=request.POST['login_email']).exists()):
            user = User.objects.filter(email=request.POST['login_email'])[0]
            hashed_pass = bcrypt.hashpw(request.POST['login_password'].encode('utf-8'), bcrypt.gensalt())
            password = user.password[2: -1]
            if (bcrypt.checkpw(request.POST['login_password'].encode('utf-8'), password.encode())):
                request.session['id'] = user.id
                return redirect('/success')

        errors = {}
        errors['email'] = "Email or password is wrong."
        for tag, error in errors.items():
            messages.error(request, error, extra_tags=tag)
            return redirect('/login')
    else:
        return render(request, 'register/login.html')

def success(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        "user": user
    }
    return render(request, 'register/success.html', context)