# Generated by Django 2.2.7 on 2019-12-23 14:17

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20191203_1653'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActicalImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flieimage', models.CharField(max_length=1000)),
                ('image_path', models.ImageField(storage=django.core.files.storage.FileSystemStorage(), upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='AticalImage',
        ),
    ]
