# Generated by Django 2.2.10 on 2020-05-02 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200502_1639'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articaltag',
            options={'verbose_name': '文章标签', 'verbose_name_plural': '文章标签'},
        ),
        migrations.AddField(
            model_name='artical',
            name='published',
            field=models.CharField(choices=[('published', '发布'), ('draft', '草稿')], default='draft', max_length=32, verbose_name='发布状态'),
            preserve_default=False,
        ),
    ]
