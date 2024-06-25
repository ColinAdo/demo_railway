from django.db import models

class Post(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} post'