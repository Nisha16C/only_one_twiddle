# Generated by Django 3.2 on 2021-05-07 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='header',
            field=models.ImageField(default='header.png', upload_to='users/headers/'),
        ),
    ]
