from django.db import models
from django.contrib.auth.models import User #,AbstractUser

# class CustomUser(AbstractUser):
#     pass


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="img/")


def __str__(self):
    return str(self.user)