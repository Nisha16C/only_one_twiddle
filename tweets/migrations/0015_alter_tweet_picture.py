# Generated by Django 3.2.4 on 2023-07-14 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0014_tweet_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='tweet/'),
        ),
    ]
