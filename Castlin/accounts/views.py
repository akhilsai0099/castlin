from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

# logging out
def logout(request):
    auth.logout(request)
    return redirect('/')


# validating login
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
            
    else:
        return render(request, 'login.html' )

#registering accounts
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request , 'username is already taken please choose another one')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request , 'An account is already associated with the given email address please try logging in instead')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email,password = password2)
                user.save()
                return redirect('login')
        else:
            messages.info(request , 'Both the passwords did not match please try again')
            return redirect('register')
    else:
        return render(request, 'register.html' )
