from typing_extensions import override
from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.TextField()


    @override
    def __str__(self) -> str:
        return self.text[:50]
