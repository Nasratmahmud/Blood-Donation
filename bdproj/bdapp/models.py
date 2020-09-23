from django.db import models

# Create your models here.
class Register(models.Model):
    fullname = models.CharField(max_length=64, blank=False)
    age = models.CharField(max_length=3, blank=False)
    gender = models.CharField(max_length=6, blank=False)
    bloodgroup = models.CharField(max_length=2, blank=False)
    contact = models.CharField(max_length=11, blank=False)
    # return title
    def __str__(self):
        return str(self.fullname)
