from django.db import models
from django.conf import settings

class Tweet(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               related_name='tweets',
                               on_delete=models.CASCADE)
    body = models.CharField(max_length=280, verbose_name="tweet")
    photo = models.ImageField(upload_to='tweet_photos/', blank=True, null=True)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                 related_name='tweets_liked',
                                 blank=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    updated = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.author.username} writes {self.body[:20]}...'

    @property
    def like_count(self):
        return self.users_like.all().count()


class Mention(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               related_name='mentions',
                               on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet,
                              related_name='mentions',
                              on_delete=models.CASCADE)
    mention = models.CharField(max_length=280, verbose_name="mention")
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                 related_name='mentions_liked',
                                 blank=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.author.username} mention to {self.tweet.body[:10]} with {self.mention[:10]}'

    @property
    def like_count(self):
        return self.users_like.all().count()

class Retweet(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               related_name='retweets',
                               on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet,
                              related_name='retweets',
                              on_delete=models.CASCADE)
    retweet = models.CharField(max_length=280, verbose_name="retweet")
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                 related_name='retweets_liked',
                                 blank=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.author.username} retweet to {self.tweet.body[:10]} with {self.retweet[:10]}'

    @property
    def like_count(self):
        return self.users_like.all().count()
