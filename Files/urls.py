from django.urls import path,include
from Files import views

app_name='Files'

urlpatterns = [
    path('add_file',views.add_file,name="add_file"),
    path('private_file',views.private_file,name="private_file"),
    path('public_file',views.public_file,name="public_file"),
    path('shaired_file',views.shaired_file,name="shaired_file"),

]