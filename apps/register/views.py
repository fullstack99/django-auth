from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.http import JsonResponse
from datetime import datetime, timedelta
import bcrypt
import jwt, json
from .models import User

def index(request):
    if request.session._session:
        return redirect('/success')
    else:
        return render(request, 'register/index.html')

def register(request):
    if request.session._session:
        return redirect('/success')

    if request.method == "POST":
        errors = User.objects.validator(request.POST)
        if len(errors):
            for tag, error in errors.items():
                messages.error(request, error, extra_tags=tag)
            error_messages = messages.get_messages(request)
            for error_message in error_messages:
                message = error_message.message

                return JsonResponse({
                    "tag": error_message.tags,
                    "message": message
                })

        exist_user = User.objects.filter(email=request.POST['email'])
        if exist_user:
            return JsonResponse({
                "tag": "email",
                "message": "This Email exists already"
            })

        hashed_password = bcrypt.hashpw(request.POST['password'].encode('utf-8'), bcrypt.gensalt())
        user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], password=hashed_password, email=request.POST['email'])
        user.save()

        token = createJWT(user)
        request.session['token'] = token
        request.session['id'] = user.id
        return JsonResponse({
            "tag": "success"
        })
    else:
        return render(request, 'register/signup.html')

def login(request):
    if request.session._session:
        return redirect('/success')

    if request.method == "POST":
        errors = {}
        if (User.objects.filter(email=request.POST['login_email']).exists()):
            user = User.objects.filter(email=request.POST['login_email'])[0]
            hashed_pass = bcrypt.hashpw(request.POST['login_password'].encode('utf-8'), bcrypt.gensalt())
            password = user.password[2: -1]
            if (bcrypt.checkpw(request.POST['login_password'].encode('utf-8'), password.encode())):
                request.session['id'] = user.id
                token = createJWT(user)
                request.session['token'] = token
                return redirect('/success')

            errors['pass'] = "Password is wrong."
        else:
            errors['email'] = "Email is wrong."

        for tag, error in errors.items():
            messages.error(request, error, extra_tags=tag)
            return redirect('/login')
    else:
        return render(request, 'register/login.html')

def success(request):
    if request.session._session:
        user = User.objects.get(id=request.session['id'])
        token = request.session.get('token')

        try:
            decode_token = jwt.decode(bytes(token, encoding='utf8'), "SECRET_KEY")
        except jwt.ExpiredSignatureError:
            print("Token expired. Get new one")
            token = createJWT(user)
        except jwt.InvalidTokenError:
            print("Invalid Token")
            token = createJWT(user)

        context = {
            "user": user,
            "token": token
        }
        request.session['token'] = token
        return render(request, 'register/success.html', context)
    else:
        return redirect('/')

def logout_view(request):
    logout(request)
    return redirect('/login')

def createJWT(user):
    payload = {
        'id': user.id,
        'email': user.email,
        'exp': datetime.utcnow() + timedelta(minutes=30)
    }
    jwt_token = {'token': jwt.encode(payload, "SECRET_KEY")}
    return jwt_token["token"].decode("utf-8")
