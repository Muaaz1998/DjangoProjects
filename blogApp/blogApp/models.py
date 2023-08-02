from typing_extensions import override
from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    body = models.TextField()

    @override
    def __str__(self) -> str:
        return self.title