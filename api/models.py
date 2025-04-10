from django.contrib.auth.models import AbstractUser
from django.db import models

#AbstractUser all builtin
#AbstractBaseUser allows full customization 
class User(AbstractUser):
    ROLE_CHOICES = [("gold", "Gold"), ("silver", "Silver"), ("bronze", "Bronze")]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="bronze")
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [] 

    def __str__(self):
        return self.email
    
class Item(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return f"{self.name} (Owner: {self.user.email})"

