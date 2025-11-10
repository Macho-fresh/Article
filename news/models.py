from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    image_url = models.URLField(null=True, blank=True)
    image_post = models.ImageField(upload_to='media/', blank=True, null=True)
    pub_date = models.CharField(max_length=100, null=True, blank=True)
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    translations = models.JSONField(default=dict, blank=True)  # stores {'fr': '...', 'es': '...'}



    def __str__(self):
        return self.title

class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'article')

    def __str__(self):
        return f'{self.user.username} bookmarked {self.article}'