# Generated by Django 3.2.4 on 2023-07-15 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_remove_message_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='messages_images/'),
        ),
    ]
