from django.shortcuts import render
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from account.models import Custom_user
# Create your views here.

def add_user(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        mobileno=request.POST['mobileno']
        role=request.POST['role']

        if Custom_user.objects.filter(username=username).exists():
            error_msg='username already exist !'
            data={'error_msg':error_msg}
            return render(request,'user/user.html',data)
        else:
            user=Custom_user.objects.create(username=username,
                                        email=email,
                                        password=make_password(password),
                                        mobaileno=mobileno,
                                        role=role) #insert data
            return HttpResponseRedirect(reverse('user:user'))
    else:
        return render(request,'user/user.html')

def user(request):
    user=Custom_user.objects.all() #to fetch all record
    date_dict={'user':user}
    return render(request,'user/user.html',date_dict)

def updateInfo(request,pk):
    user1=Custom_user.objects.get(pk=pk)
    if request.method == 'POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        mobileno=request.POST['mobileno']
        user1.first_name=firstname
        user1.last_name=lastname
        user1.username=username
        user1.email=email
        user1.mobaileno=mobileno
        user1.save()
        return HttpResponseRedirect(reverse('user:user'))

def user_delete(request,pk):
    user_object = Custom_user.objects.get(pk=pk)
    user_object.delete()
    return HttpResponseRedirect(reverse('user:user'))