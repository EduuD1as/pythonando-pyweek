from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
    
        if senha != confirmar_senha:
            return redirect('/users/signup')
        
        if len(senha) < 8:
            return redirect('/users/signup')
        
        users = User.objects.filter(username=username)
        
        if users.exists():
            return redirect('/users/signup')
    
        User.objects.create_user(
            username=username,
            password=senha
        )
        
        return redirect('/users/login')