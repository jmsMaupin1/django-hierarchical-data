from django.db import models
from django.contrib.auth.models import AbstractUser

from file.models import File


# Create your models here.
class User(AbstractUser):
    folder = models.OneToOneField(File, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.folder = File.objects.create(
                name="{}'s folder".format(self.username),
                parent=None
            ) 
            super().save(*args, **kwargs)