from unicodedata import category
from xml.dom import ValidationErr
from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.
cloth_types=(('NEW','NEW'), ('bestseller','bestseller'))

class UserManager(BaseUserManager):

    def create_user(self,email,password=None, **extrafields):
        if not email:
            raise ValueError("Email is required")
        user=self.model(email=self.normalize_email(email), **extrafields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password):
        user=self.create_user(email,password)
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    firstname = models.CharField(max_length=200,blank=True)
    lastname = models.CharField(max_length=3000,blank=True)
    email = models.EmailField(max_length=4000, unique=True)
    address = models.TextField(max_length=4000,blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return f'{self.firstname}'

class Category(models.Model):
    name = models.CharField(max_length=200,null=True)
    

    def __str__(self):
        return f'{self.name}'
    
   

class Item(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    cloths_tags = models.CharField(max_length=2000,choices=cloth_types,null=True)
    is_discount=models.BooleanField(default=True)
    cloth_price=models.CharField(max_length=2000,null=True)
    discount_price=models.CharField(max_length=2000,blank=True,null=True)
    image_url=models.ImageField(null=True)
    description = models.TextField(max_length=2000,null=True)
    product_name=models.CharField(max_length=2000,null=True)

    def __str__(self):
        return f'{self.category.name}'