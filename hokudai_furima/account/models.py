from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.db import models
from django.forms.models import model_to_dict
from django.utils import timezone
from django.utils.translation import pgettext_lazy
from django.contrib.auth.validators import UnicodeUsernameValidator
from django import forms

class UserManager(BaseUserManager):

    def create_user(
            self, username, email, password=None,
            **extra_fields):       
        email = UserManager.normalize_email(email)
        user = self.model(
            username=username, email=email,
            **extra_fields)
        if password:
            user.set_password(password)
        user.save()
        return user


class User(PermissionsMixin, AbstractBaseUser):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        ('username'),
        max_length=150,
        unique=True,
        help_text=(
            'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': ("A user with that username already exists."),
        },
    )
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    intro = models.TextField(('intro'), max_length=200, blank=True)
    date_joined = models.DateTimeField(default=timezone.now, editable=False)
    # 画像など、テキストフィールドを使わない場合どうする？
    #icon = 
    #is_staff = models.BooleanField(default=False)
    #is_active = models.BooleanField(default=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    #REQUIRED_FIELDS = ['password1','password2']

    objects = UserManager()


