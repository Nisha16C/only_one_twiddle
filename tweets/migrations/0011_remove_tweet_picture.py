# Generated by Django 3.2.4 on 2023-07-13 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0010_alter_tweet_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='picture',
        ),
    ]
