# Generated by Django 2.0 on 2020-02-14 08:17

import django.core.files.storage
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20191223_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='artical',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='添加时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artical',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='acticalimage',
            name='image_path',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage('/home/jhw/code/django-demo/media'), upload_to=''),
        ),
    ]