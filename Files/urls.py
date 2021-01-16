from django.urls import path,include
from Files import views

app_name='Files'

urlpatterns = [
    path('add_file',views.add_file,name="add_file"),
    path('private_file',views.private_file,name="private_file"),
    path('public_file',views.public_file,name="public_file"),
    path('shared_file',views.shared_file,name="shared_file"),
    path('share_submit/<int:pk>',views.share_submit,name="share_submit"),
    

]