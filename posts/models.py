# Posts models

#Django
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    caption = models.CharField(max_length=240)
    photo = models.ImageField(upload_to='posts/src')
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} by @{}'.format(self.caption, self.user.username)