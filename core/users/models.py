from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self,username,email,name,password=None):
        if not email:
            raise ValueError('you need to provide an email')
        user = self.model(
            username = username,
            email = self.normalize_email(email),
            name = name
        )
        user.setpassword(password)
        user.save()
        return user
    
    def create_superuser(self, username, email, name, password):
        user = self.create_user(
            email,
            username=username,
            name=name,
            password=password,
        )

        user.staff = True
        user.save()
        return user

class User(AbstractUser):
    username = models.CharField('Username', max_length=75,unique=True)
    email = models.EmailField('Email', max_length=254,unique=True)
    name = models.CharField('Name', max_length=75,unique=True)
    image = models.ImageField('Image', upload_to='profile')
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, usuarios_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_staff

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','name']