from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Custom_user(AbstractUser):
      # Datafields
      ADMIN = 1
      TEAM_MEMBER = 2
      ROLE_CHOICES = (
        (ADMIN,'admin'),
        (TEAM_MEMBER,'team_member'),
      )
      #This field store User's Role
      role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES,default=TEAM_MEMBER)
      mobaileno=models.CharField(max_length=20,default='9874563210')
      created_at=models.DateTimeField(auto_now=True)
      updated_at=models.DateTimeField(auto_now=True)

      def __str__(self):
            return str(self.pk)
            
class Member(models.Model):
      custom_user=models.OneToOneField(Custom_user,on_delete=models.CASCADE)
      created_at=models.DateTimeField(auto_now=True)
      updated_at=models.DateTimeField(auto_now=True)

      def __str__(self):
          return str(self.pk)
