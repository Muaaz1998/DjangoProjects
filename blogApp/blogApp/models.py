from typing_extensions import override
from django.db import models
from django.urls import reverse

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    body = models.TextField()
    

    # @override
    # def get_absolute_url(self):
    #     return f"/post/{self.id}/"

    # A better way to do this is to use reverse. 
    # Improves portability
    @override
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk" : self.pk})

    @override
    def __str__(self) -> str:
        return self.title