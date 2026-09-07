from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to="profile_images/",
        default="profile_images/default.jpg",
        blank=True,
        null=True,
    )
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Profile of {self.user.username}"
