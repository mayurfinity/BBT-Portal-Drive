# Generated by Django 3.1.3 on 2021-01-09 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='custom_user',
            name='mobaileno',
            field=models.CharField(default='9874563210', max_length=20),
        ),
    ]