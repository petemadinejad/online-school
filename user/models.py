from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import BaseModel


class User(AbstractUser):
    """
    Custom User Model
    """
    REQUIRED_FIELDS = ['phone_number']
    phone_number = models.CharField(max_length=20, verbose_name=_('Phone'))

    class Meta:
        db_table = 'user'
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.username
