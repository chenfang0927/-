# Generated by Django 2.2.13 on 2020-08-10 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='姓名')),
                ('age', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='年龄')),
                ('mailbox', models.CharField(max_length=50, unique=True, verbose_name='邮箱')),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]