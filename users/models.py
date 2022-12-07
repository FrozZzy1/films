from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from django.db import models
from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFill


class UserManager(BaseUserManager):
    def create_user(self, username, email, password):
        if not username:
            raise TypeError('Users must have a username')
        if not email:
            raise TypeError('Users must have an email address')
        if not password:
            raise TypeError('Users must have a password')

        user = self.model(username=username,
                          email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('username', max_length=20, unique=True)
    email = models.CharField('email', max_length=100, unique=True, db_index=True)
    avatar = ProcessedImageField(
        format='PNG',
        processors=[
            ResizeToFill(50, 50)
        ],
        verbose_name='Аватарка пользователя',
        blank=True,
        null=True
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_subscription_newsletter = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email
