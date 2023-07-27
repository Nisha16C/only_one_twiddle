from django.contrib import admin

from .models import Tweet, Mention, Retweet

@admin.register(Mention)
class MentionAdmin(admin.ModelAdmin):
    list_display = ('author', 'tweet', 'get_mention', 'like_count', 'created')
    list_filter = ('created',)
    search_fields = ('mention', 'tweet')

    def get_mention(self, instance):
        return instance.mention[:20] + ' ...'
    get_mention.short_description = 'Mention'

@admin.register(Retweet)
class RetweetAdmin(admin.ModelAdmin):
    list_display = ('author', 'tweet', 'get_retweet', 'like_count', 'created')
    list_filter = ('created',)
    search_fields = ('retweet', 'tweet')

    def get_retweet(self, instance):
        return instance.retweet[:20] + ' ...'
    get_retweet.short_description = 'retweet'
    
@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ('author', 'get_body', 'like_count', 'created')
    list_filter = ('created',)
    search_fields = ('body',)

    def get_body(self, instance):
        return instance.body[:20] + ' ...'
    get_body.short_description = 'Body'
