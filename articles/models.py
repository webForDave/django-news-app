from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Articles(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])