from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


#the base user which has username, email_id. This is used for client.
class User(AbstractUser):
    isauthor =models.BooleanField(default=False)
    iseditor=models.BooleanField(default=False)
    isreviewer=models.BooleanField(default=False)
    isuser=models.BooleanField(default=False)
    contact=models.CharField(max_length=10)
    
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)    
    field=models.CharField(max_length=100)
    affliation=models.CharField(max_length=200)
    country= models.CharField(max_length=100, default="")
    def __str__(self):
        return self.user.username
    
    

class Reviewer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    field=models.CharField(max_length=100)

    
    def __str__(self):
        return self.user.username
    

    

class Editor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    

    




    

