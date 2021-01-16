
from django.shortcuts import render
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from Files.models import Files
from account.models import Member
from permissions.models import Permission
# Create your views here.

def shared_file_per(request,pk):
    file_object=Files.objects.get(pk=pk)
    data_dict={'file_object':file_object}
    return render(request, "Files/shared_file.html",data_dict)

# def share_submit(request,pk):
#     file_object=Files.objects.get(pk=pk)
#     if request.method == "POST":
#         member_object=request.POST['username']
#         member=Member.Objects.get(pk=member_object)
#         permission_object=Permission.objects.create(file_object=file_object,
#                                                     member_object=member_object
#                                                     )
#         return HttpResponseRedirect(reverse('Files:private_file'))
#     return render(request, "Files/private_file.html")