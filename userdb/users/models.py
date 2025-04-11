from django.db import models

# Create your models here.
from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    enroll = models.CharField(max_length=20, unique=True)
    age = models.PositiveIntegerField()
    branch = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.enroll})"
