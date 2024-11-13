from django.db import models

# Create your models here.
class Communication(models.Model):
    #This is my communication table
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15) 
    message = models.TextField()
    date = models.DateField()


    def __str__(self):
        return f"{self.name} - {self.email}"
