from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120) 
    description = models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.name +' : '+ self.email