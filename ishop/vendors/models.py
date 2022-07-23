from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Vendor(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        ordering=['user']

    def __str__(self):
        return self.user.email