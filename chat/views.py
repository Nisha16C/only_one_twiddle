# from django.shortcuts import render

# # Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from .models import Chat, Message
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
# from django.db.models import Count

# Import the Q object here

@login_required
def user_list(request):
    current_user = request.user

    # Get all users excluding the current user
    users = User.objects.exclude(id=current_user.id)

    # Iterate through each user and get their unread message count to the current user
    for user in users:
        unread_count = Message.objects.filter(sender=user, receiver=current_user, is_read=False).count()
        user.unread_count = unread_count

    # Calculate the total unread messages count from all senders to the current user
    total_unread_count = Message.objects.filter(receiver=current_user, is_read=False).count()

    return render(request, 'chat/user_list.html', {'users': users, 'total_unread_count': total_unread_count})

@login_required
def send_message(request, user_id):
    receiver = get_object_or_404(User, id=user_id)
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


