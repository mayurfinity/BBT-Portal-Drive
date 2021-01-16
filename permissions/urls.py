from django.urls import path,include
from permissions import views

app_name='permissions'

urlpatterns = [
    path('shared_file_per',views.shared_file_per,name="shared_file_per"),
    # path('share_submit/<int:pk>',views.share_submit,name="share_submit"),
]