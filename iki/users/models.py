from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.



class User(AbstractUser):
    bio = models.CharField(max_length=160, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username']

    image = models.ImageField(
        upload_to='users/',
        verbose_name='image'
    )
    email = models.EmailField(max_length=30, unique=True, blank=True)

    def __str__(self):
        return self.username
