from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class OwnerUrls(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    long_url = models.CharField(max_length=200, null=True, blank=True)
    short_url = models.CharField(max_length=50, null=True, blank=True)
    

    def __str__(self):
        return str(self.long_url)

    def get_absolute_url(self):
        return f'/url/{self.short_url}'