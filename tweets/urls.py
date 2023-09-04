from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('tweet/', views.create_tweet, name="create_tweet"),
    path('delete/', views.delete_tweet, name="delete_tweet"),
    path('like-unlike/', views.like_unlike, name="like-unlike"),
    path('<int:pk>/', views.tweet_detail, name="tweet_detail"),
    path('<int:tweet_id>/mention/', views.create_mention, name="create_mention"),
    path('<int:tweet_id>/retweet/', views.create_retweet, name="create_retweet"),
    path('search/', views.search, name="search"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
