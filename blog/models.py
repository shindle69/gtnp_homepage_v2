from django.db import models
from askcompany.utils import uuid_upload_to


class Post(models.Model):    
    title = models.CharField(max_length=100)
    content = models.TextField()    
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

