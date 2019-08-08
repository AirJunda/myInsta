from django.db import models
from django.urls import reverse

#from django.contrib.auth.models import User
from imagekit.models import ProcessedImageField
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Post(models.Model):
    title = models.TextField(blank=True,null=True)
    
    image = ProcessedImageField(
        upload_to = 'static/images/posts',
        format = 'JPEG',
        options={'quality':100},
        blank=True,
        null = True
    )

# this mehtod is to allow the page to redirect to a pre-defined page after submiting the form. Here, we aim to
# direct it to the post just submitted. 
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)]) 

class InstaUser(AbstractUser):
    profile_pic = ProcessedImageField(
        upload_to = 'static/images/profile_users',
        format = 'JPEG',
        options={'quality':100},
        blank=True,
        null = True
        )
