# Generated by Django 2.2.13 on 2020-09-01 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='文章标题')),
                ('category', models.CharField(max_length=20, verbose_name='文章分类')),
                ('limit', models.CharField(max_length=20, verbose_name='文章权限')),
                ('introduce', models.CharField(max_length=30, verbose_name='文章简介')),
                ('content', models.TextField(verbose_name='文章内容')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserProfile')),
            ],
        ),
    ]
