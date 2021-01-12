from django.urls import path,include
from account import views

app_name='account'

urlpatterns = [
    path('user_login',views.user_login,name='user_login'),
    path('index',views.index,name='index'),
    path('profile',views.profile,name='profile'),
    path('logout',views.logout,name='logout'),
    # path('forget_password',views.forget_password,name='forget_password'),

    # path('updateInfo/<int:pk>',views.updateInfo,name="updateInfo"), 
]