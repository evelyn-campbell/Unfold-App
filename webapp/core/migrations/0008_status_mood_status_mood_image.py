# Generated by Django 4.0.4 on 2022-08-28 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_status_mood'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='mood',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='status',
            name='mood_image',
            field=models.ImageField(default='happy.png', upload_to='mood_pictures'),
        ),
    ]
