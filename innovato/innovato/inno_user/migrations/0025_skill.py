# Generated by Django 3.0.8 on 2021-03-22 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inno_user', '0024_auto_20210320_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('sk_id', models.AutoField(primary_key=True, serialize=False)),
                ('sk_user', models.CharField(default='', max_length=30)),
                ('Html', models.CharField(default='', max_length=10)),
                ('Css', models.CharField(default='', max_length=10)),
                ('Js', models.CharField(default='', max_length=10)),
                ('Python', models.CharField(default='', max_length=10)),
                ('Database', models.CharField(default='', max_length=10)),
                ('Wordpress', models.CharField(default='', max_length=10)),
                ('Mongodb', models.CharField(default='', max_length=10)),
            ],
        ),
    ]