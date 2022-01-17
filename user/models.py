from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class CustomAccountManager(BaseUserManager):
    ''' Creating a UserManagerClass for the CasinoUser Class: Admin Dashboard at ./admins.py '''

    def create_superuser(self, email, user_name, first_name, last_name, password, **other_fields):
        ''' Creating the SuperUser -> python manage.py createsuperuser '''
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name, last_name, 100000, password, **other_fields)

    def create_user(self, email, user_name, first_name, last_name, balance, password, **other_fields):
        ''' Create default User '''
        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, last_name=last_name, balance=balance ,**other_fields)
        user.set_password(password)
        user.save()
        return user

class CasinoUser(AbstractBaseUser, PermissionsMixin):
    ''' Creating a custom User class from the AbstractBaseUser class of Django '''

    email       = models.EmailField(_('email address'), unique=True, primary_key=True)
    user_name   = models.CharField(max_length=50)
    first_name  = models.CharField(max_length=50)
    last_name   = models.CharField(max_length=50)
    balance     = models.IntegerField(default=0)
    is_staff    = models.BooleanField(default=False)
    is_active   = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name', 'last_name']

    def __str__(self):
        return self.email