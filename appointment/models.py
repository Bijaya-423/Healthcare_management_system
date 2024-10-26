from django.db import models

# Create your models here.


class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    department = models.CharField(max_length=50)

    def __str__(self):
        return f'Appointment for {self.name} on {self.date} at {self.time}'
