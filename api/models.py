from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.base_user import BaseUserManager

#AbstractUser all builtin
#AbstractBaseUser allows full customization 

class UserManager(BaseUserManager):
     def create_user(self, email, password=None, role="bronze", **extra_fields):
         if not email:
             raise ValueError("Email is required")
         email = self.normalize_email(email)
         user = self.model(email=email, role=role, **extra_fields)
         user.set_password(password)
         user.save(using=self._db)
         return user
 
     def create_superuser(self, email, password=None, **extra_fields):
         extra_fields.setdefault("is_staff", True)
         extra_fields.setdefault("is_superuser", True)
         return self.create_user(email, password, role="gold", **extra_fields)

class User(AbstractUser):
    ROLE_CHOICES = [("gold", "Gold"), ("silver", "Silver"), ("bronze", "Bronze")]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="bronze")
    email = models.EmailField(unique=True)

    username = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [] 

    objects = UserManager()

    def __str__(self):
        return self.email
    
class Item(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return f"{self.name} (Owner: {self.user.email})"

