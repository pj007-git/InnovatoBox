# Generated by Django 3.1.7 on 2021-04-08 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inno_user', '0028_video_up_v_gif'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video_up',
            name='v_gif',
            field=models.ImageField(upload_to='inno_user/Gif/'),
        ),
    ]
