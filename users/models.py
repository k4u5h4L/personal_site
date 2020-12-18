from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):

    pass

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE)

    image = models.ImageField(default='default_profile_pic.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'