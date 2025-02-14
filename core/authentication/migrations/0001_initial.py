# Generated by Django 5.1.6 on 2025-02-14 19:07

import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=255)),
                ('turma', models.CharField(choices=[('1info1', '1info1'), ('1info2', '1info2'), ('1info3', '1info3'), ('2info1', '2info1'), ('2info2', '2info2'), ('2info3', '2info3'), ('3info1', '3info1'), ('3info2', '3info2'), ('3info3', '3info3'), ('1agro1', '1agro1'), ('1agro2', '1agro2'), ('1agro3', '1agro3'), ('2agro1', '2agro1'), ('2agro2', '2agro2'), ('2agro3', '2agro3'), ('3agro1', '3agro1'), ('3agro2', '3agro2'), ('3agro3', '3agro3'), ('1quimi', '1quimi'), ('2quimi', '2quimi'), ('3quimi', '3quimi')], max_length=6)),
                ('curso', models.CharField(choices=[('informatica', 'Informatica Para Internet'), ('quimica', 'Quimica'), ('agropecuaria', 'Agropecuaria')], max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GuildMemberData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_active', models.IntegerField(blank=True, null=True)),
                ('verification_token', models.CharField(blank=True, max_length=100, null=True)),
                ('verified', models.BooleanField(default=False)),
                ('office', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='authentication.office')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authentication.student')),
            ],
        ),
    ]
