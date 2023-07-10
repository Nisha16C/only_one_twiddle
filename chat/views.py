# from django.shortcuts import render

# # Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from .models import Chat, Message
from django.contrib.auth.decorators import login_required
from django.db.models import Count


# @login_required
# def user_list(request):
#     users = User.objects.exclude(id=request.user.id)
#     chats = Chat.objects.filter(participants=request.user).annotate(num_participants=Count('participants')).filter(num_participants=2)
#     return render(request, 'chat/user_list.html', {'users': users, 'chats': chats})



# @login_required
# def user_list(request):
#     users = User.objects.exclude(id=request.user.id)
#     return render(request, 'chat/user_list.html', {'users': users})


# def user_list(request):
#     users = User.objects.exclude(id=request.user.id)
#     chats = Chat.objects.filter(participants=request.user)
#     return render(request, 'chat/user_list.html', {'users': users, 'chats': chats})

@login_required
def user_list(request):
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'chat/user_list.html', {'users': users})

# @login_required
# def send_message(request, user_id):
#     receiver = get_object_or_404(User, id=user_id)
#     sender = request.user

#     chat = Chat.objects.filter(participants=sender).filter(participants=receiver).first()
#     if not chat:
#         chat = Chat.objects.create()
#         chat.participants.add(sender, receiver)

#     if request.method == 'POST':
#         content = request.POST['content']
#         message = Message.objects.create(sender=sender, receiver=receiver, content=content)
#         chat.messages.add(message)
#         chat.save()
#         return redirect('user_list')

#     messages = chat.messages.all() if chat else []
#     return render(request, 'chat/send_message.html', {'receiver': receiver, 'messages': messages})
@login_required
def send_message(request, user_id):
    receiver = get_object_or_404(User, id=user_id)
    sender = request.user

    chat = Chat.objects.filter(participants=sender).filter(participants=receiver).first()
    if not chat:
        chat = Chat.objects.create()
        chat.participants.add(sender, receiver)

    if request.method == 'POST':
        content = request.POST['content']
        message = Message.objects.create(sender=sender, receiver=receiver, content=content)
        chat.messages.add(message)
        chat.save()
        return redirect('send_message', user_id=user_id)

    messages = chat.messages.order_by('timestamp') if chat else []
    return render(request, 'chat/send_message.html', {'receiver': receiver, 'messages': messages})


# @login_required
# def send_message(request, user_id):
#     receiver = get_object_or_404(User, id=user_id)
#     sender = request.user

#     chat = Chat.objects.filter(participants=sender).filter(participants=receiver).first()
#     if not chat:
#         chat = Chat.objects.create()
#         chat.participants.add(sender, receiver)

#     if request.method == 'POST':
#         content = request.POST['content']
#         message = Message.objects.create(sender=sender, receiver=receiver, content=content)
#         chat.messages.add(message)
#         chat.save()
#         return redirect('user_list')

#     messages = chat.messages.all() if chat else []
#     return render(request, 'chat/send_message.html', {'receiver': receiver, 'messages': messages})

# def send_message(request, user_id):
#     receiver = get_object_or_404(User, id=user_id)
#     sender = request.user

#     chat = Chat.objects.filter(participants=sender).filter(participants=receiver).first()
#     if not chat:
#         chat = Chat.objects.create()
#         chat.participants.add(sender, receiver)

#     if request.method == 'POST':
#         content = request.POST['content']
#         message = Message.objects.create(sender=sender, receiver=receiver, content=content)
#         chat.messages.add(message)
#         chat.save()
#         return redirect('user_list')

#     messages = chat.messages.all() if chat else []
#     return render(request, 'chat/send_message.html', {'receiver': receiver, 'messages': messages})

# def send_message(request, user_id):
#     receiver = get_object_or_404(User, id=user_id)

#     if request.method == 'POST':
#         content = request.POST['content']
#         sender = request.user

#         message = Message.objects.create(sender=sender, receiver=receiver, content=content)

#         # Create or get the chat between the sender and receiver
#         chat = Chat.objects.filter(participants=sender).filter(participants=receiver).first()
#         if not chat:
#             chat = Chat.objects.create()
#             chat.participants.add(sender, receiver)

#         chat.messages.add(message)
#         chat.save()

#         return redirect('user_list')

#     return render(request, 'chat/send_message.html', {'receiver': receiver})

