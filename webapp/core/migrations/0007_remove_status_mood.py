# Generated by Django 4.0.4 on 2022-08-28 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_profile_friends_friendrequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='mood',
        ),
    ]
