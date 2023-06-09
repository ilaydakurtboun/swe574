# Generated by Django 3.1.1 on 2023-04-04 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_friendrequest_friends'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='photo',
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.FileField(blank=True, null=True, upload_to='avatar'),
        ),
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
    ]
