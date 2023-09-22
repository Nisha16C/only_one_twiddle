# new_app/views.py
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from chat.models import Chat, Message
from django.contrib.auth.decorators import login_required
from django.db.models import Count


user_rec = []
@login_required
def delete_message_view(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    
    # Check if the logged-in user is the sender or receiver of the message
    if request.user == message.sender or request.user == message.receiver:
        message.delete()
        # return redirect('home')
        user_id = message.receiver.id if request.user == message.sender else message.sender.id
        return redirect('send_message', user_id=user_id)


@login_required
def send_message_view(request, user_id):
    receiver = get_object_or_404(User, id=user_id)
    user_rec.append(receiver)
    sender = request.user

    chat = Chat.objects.filter(participants=sender).filter(participants=receiver).first()
    if not chat:
        chat = Chat.objects.create()
        chat.participants.add(sender, receiver)

    # Mark messages as read when the user clicks on the user
    unread_messages = Message.objects.filter(sender=receiver, receiver=sender, is_read=False)
    unread_messages.update(is_read=True)
    
    if request.method == 'POST':
        content = request.POST['content']
        image =  request.FILES.get('image')
        message = Message.objects.create(sender=sender, receiver=receiver, content=content, image=image)
        chat.messages.add(message)
        chat.save()
        return redirect('send_message', user_id=user_id)

    messages = chat.messages.order_by('timestamp') if chat else []
    return render(request, 'chat/newUi.html', {'receiver': receiver, 'messages': messages})



