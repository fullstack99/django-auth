from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.http import JsonResponse
from datetime import datetime, timedelta
from django.core import serializers

from django.contrib.auth.models import User
from rest_framework import viewsets
# from .serializers import UserSerializer

import bcrypt
import jwt, json

from .models import User
from .form import userForm

def index(request):
    if request.session._session:
        return redirect('/success')
    else:
        return render(request, 'index.html')

def register(request):
    json_data = json.loads(request.body)
    errors = User.objects.validator(json_data)
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error, extra_tags=tag)
        error_messages = messages.get_messages(request)
        for error_message in error_messages:
            message = error_message.message

            return JsonResponse({
                "error": message
            }, status=400)

    exist_user = User.objects.filter(email=json_data['email'])
    if exist_user:
        return JsonResponse({
            "error": "This Email exists already"
        }, status=400)

    hashed_password = bcrypt.hashpw(json_data['password'].encode('utf-8'), bcrypt.gensalt())
    user = User.objects.create(
        first_name=json_data['firstName'],
        last_name=json_data['lastName'],
        password=hashed_password, email=json_data['email']
    )
    user.save()

    token = createJWT(user)
    request.session['token'] = token
    data = serializers.serialize('json', [user])
    return JsonResponse({
        "token": token,
        "user": data[1: -1]
    })

def login(request):
    json_data = json.loads(request.body)
    errors = {}
    if (User.objects.filter(email=json_data['email']).exists()):
        user = User.objects.filter(email=json_data['email'])[0]
        hashed_pass = bcrypt.hashpw(json_data['password'].encode('utf-8'), bcrypt.gensalt())
        password = user.password[2: -1]
        if (bcrypt.checkpw(json_data['password'].encode('utf-8'), password.encode())):
            request.session['id'] = user.id
            token = createJWT(user)
            request.session['token'] = token
            data = serializers.serialize('json', [user])

            return JsonResponse({
                "token": token,
                "user": data[1: -1]
            })

        return JsonResponse({
            "error": "Password is wrong."
        }, status=400)
    else:
        return JsonResponse({
            "error": "This user does not exist."
        }, status=404)

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
            "currentUser": user,
            "token": token
        }
        request.session['token'] = token

        if user.permission == 'admin':
            allUsers = User.objects.all()
            context = {
                "currentUser": user,
                "token": token,
                "users": allUsers
            }

        return render(request, 'dashboard.html', context)
    else:
        return redirect('/')

def logout_view(request):
    logout(request)
    return redirect('/login')

def createJWT(user):
    payload = {
        'id': user.id,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'exp': datetime.utcnow() + timedelta(minutes=30)
    }
    jwt_token = {'token': jwt.encode(payload, "SECRET_KEY")}
    return jwt_token["token"].decode("utf-8")

def userUpdate(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        "user": user,
    }
    errors = {}
    if request.method == "POST":
        user.dob = request.POST['dob']
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        if user.email != request.POST['email']:
            exist_user = User.objects.filter(email=request.POST['email'])
            if exist_user:
                errors['email'] = "This emails already exits."
                for tag, error in errors.items():
                    messages.error(request, error, extra_tags=tag)
                    return redirect('/user/update')

        user.email = request.POST['email']

        MyProfileForm = userForm(request.POST, request.FILES)
        if MyProfileForm.is_valid():
            user.picture = MyProfileForm.cleaned_data["picture"]

        user.save()

        return redirect('/success')
    else:
        return render(request, 'user/update.html', context)

def userCreate(request):
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

        return JsonResponse({
            "tag": "success"
        })
    else:
        return render(request, 'user/create.html')

def userDelete(request, user_id):
    saved = False
    user = User.objects.get(id=user_id)
    response = {
        "success": True
    }
    try:
        user.delete()
    except:
        response = {
            "success": False
        }

    return redirect('/success')

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer