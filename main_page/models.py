
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100,default=None)
    email = models.EmailField(default=None)
    phone_number = models.CharField(max_length=15,default=None)
    enquiry = models.TextField(default=None)

    def __str__(self):
        return self.name
