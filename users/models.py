from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    image = models.ImageField(
    upload_to='profiles/',
    null=True,
    blank=True,
    )

    bio = models.TextField(
        blank=True
    )

    website = models.URLField(
        blank=True
    )

    github = models.URLField(
        blank=True
    )

    linkedin = models.URLField(
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.user.username