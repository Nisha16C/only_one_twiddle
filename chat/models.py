# from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    image = models.ImageField(upload_to='messages_images/', null=True, blank=True)
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender.username} -> {self.receiver.username}'



    # def __str__(self):
    #     return f'{self.sender.username} -> {self.receiver.username}'
    
class Chat(models.Model):
    participants = models.ManyToManyField(User, related_name='chats')
    messages = models.ManyToManyField(Message)

    def __str__(self):
        usernames = [user.username for user in self.participants.all()]
        return ', '.join(usernames)
