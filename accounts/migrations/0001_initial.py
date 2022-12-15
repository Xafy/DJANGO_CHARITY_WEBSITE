# Generated by Django 3.1.7 on 2021-06-02 07:59

import datetime
from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('user_name', models.CharField(max_length=120, unique=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('full_name', models.CharField(max_length=254)),
                ('bio', models.TextField(blank=True, max_length=511, null=True)),
                ('avatar_thumbnail', imagekit.models.fields.ProcessedImageField(default='/img/default.png', upload_to='img/')),
                ('contact_information', models.TextField(blank=True, null=True)),
                ('location', models.TextField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=245, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GuestEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('active', models.BooleanField(default=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
