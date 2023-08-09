from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from chat.views import user_list, send_message

import debug_toolbar

urlpatterns = [
    # Debug toolbar
    path('__debug__/', include(debug_toolbar.urls)),

    # Django Admin
    path('admin/', admin.site.urls),

    # User profiles
    path('my/', include('profiles.urls')),

    # User management
    path('accounts/', include('allauth.urls')),

    # notifications
    path('', include('actions.urls')),
    # Pages app
    path('', include('pages.urls')),
    path('', include('mobile_otp.urls')),
   

    # Tweet stuff
    path('compose/', include('tweets.urls')),

    # # Chat app
    path('chat/', include("chat.urls")),

    path('social-auth/', include('social_django.urls', namespace='social')),

    

]

if settings.DEBUG:
    # For serving media files in development
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
