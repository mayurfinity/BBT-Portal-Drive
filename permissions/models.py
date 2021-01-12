from django.db import models


# Create your models here.
class Permission(models.Model):
    File_object =models.ForeignKey("Files.Files",on_delete=models.CASCADE)
    member =models.ForeignKey("account.Member",on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk)


