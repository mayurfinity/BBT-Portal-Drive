from django.shortcuts import render,redirect
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from account.models import Custom_user

def index(request):
    return render(request,'account/index.html')

def user_login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None :
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('account:index'))
            else :
                error_msg='username and password wrong  !'
                data={'error_msg':error_msg}
                return render(request,'account/login.html',data)
        else:
            error_msg='username and password wrong  !'
            data={'error_msg':error_msg}
            return render(request,'account/login.html',data)
    else:
        return render(request,'account/login.html')

def profile(request):
    user = request.user #to fetch all record
    date_dict={'user':user}
    return render(request,'account/profile.html')

def logout(request):
    request.session.clear()
    return HttpResponseRedirect(reverse('account:user_login'))

# def updateInfo(request,pk):
#     user1=finity_user.objects.get(pk=pk)
#     if request.method == 'POST':
#         firstname=request.POST['firstname']
#         lastname=request.POST['lastname']
#         username=request.POST['username']
#         email=request.POST['email']
#         mobileno=request.POST['mobileno']
#         user1.first_name=firstname
#         user1.last_name=lastname
#         user1.username=username
#         user1.email=email
#         user1.mobaileno=mobileno  
#         user1.save()
#         return HttpResponseRedirect(reverse('user:user'))


