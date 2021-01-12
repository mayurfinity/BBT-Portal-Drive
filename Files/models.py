from django.db import models

# Create your models here.
class Files(models.Model):
    PUBLIC = 1
    PRIVATE = 2
    FILE_TYPE = (
      (PUBLIC,'public'),
      (PRIVATE,'private'),
    )
    user_id=models.ForeignKey("account.Custom_user", on_delete=models.CASCADE)
    filename=models.CharField( max_length=50)
    filedescription=models.CharField( max_length=500)
    filetype = models.PositiveSmallIntegerField(choices=FILE_TYPE ,default=PUBLIC)
    uploadfile=models.FileField(upload_to='project_files')
    created_at=models.DateTimeField(auto_now=True)
    update_at=models.DateTimeField(auto_now=True)