from django.db import models

# Create your models here.
class Main_contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30,primary_key=True)
    subject=models.CharField(max_length=30)
    website=models.CharField(max_length=30)
    message=models.CharField(max_length=30)
    
    
    def __str__(self):
        return self.name
