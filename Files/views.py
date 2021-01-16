from django.shortcuts import render
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from Files.models import Files
from account.models import Member
from permissions.models import Permission
# Create your views here.
def add_file(request):
    Custom_user=request.user
    if request.method == 'POST':
        filename=request.POST['filename']
        filetype=request.POST['filetype']
        filedescription=request.POST['filedescription']
        uploadfile=request.FILES['uploadfile']


        file=Files.objects.create(user_id=Custom_user,
                                        filename=filename,
                                        filetype=filetype,
                                        filedescription=filedescription,
                                        uploadfile=uploadfile) #insert data
        return HttpResponseRedirect(reverse('Files:add_file'))
    else:
        return render(request,'Files/add_file.html')


def public_file(request):
    public_file=Files.objects.all().filter(filetype=1)  #to fetch all record
    date_dict={'public_file':public_file}
    return render(request,"Files/public_file.html",date_dict)

def private_file(request):
    member_object=Member.objects.all()
    private_file=Files.objects.all().filter(filetype=2,user_id=request.user) #to fetch all record
    date_dict={'private_file':private_file ,'member':member_object}
    return render(request,"Files/private_file.html",date_dict)

def shared_file(request):
    member_object=Member.objects.get(custom_user=request.user) #to fetch perticular  records
    permission_object=Permission.objects.all().filter(member=member_object)
    data_dict={'permission_object':permission_object}
    return render(request,"Files/shared_file.html",data_dict)



def share_submit(request,pk):
    File_object=Files.objects.get(pk=pk)
    if request.method == "POST":
        member=request.POST['username']
        member_object=Member.objects.get(pk=member)

        Permission.objects.create(File_object=File_object,
                                  member=member_object)
        
        return HttpResponseRedirect(reverse('Files:private_file'))
    return render(request, "Files/private_file.html")

















# def share(request,pk):
#     if request.method == "POST":
#         member_object=request.POST['username']
#         member=Member.Objects.get(pk=member_object)
#         permission_object=Permission.objects.create(file_object=file_object,
#                                                     member_object=member_object,
#                                                     )
#         return HttpResponseRedirect(reverse('Files:shared_file'))
#     return render(request, "Files/shared_file.html")
