# Generated by Django 3.1.7 on 2021-03-30 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='image',
            field=models.ImageField(upload_to='youtube/images/'),
        ),
    ]
