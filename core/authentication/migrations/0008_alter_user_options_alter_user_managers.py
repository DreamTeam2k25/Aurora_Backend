# Generated by Django 5.1.5 on 2025-01-26 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_alter_guildmemberdata_year_active_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
    ]
