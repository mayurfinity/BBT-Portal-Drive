from django.urls import path,include
from user import views

app_name='user'

urlpatterns = [
    path('user',views.user,name="user"),

    path('add_user',views.add_user,name="add_user"),

    path('updateInfo/<int:pk>',views.updateInfo,name="updateInfo"), 

    path('user_delete/<int:pk>',views.user_delete,name="user_delete"), 
]
