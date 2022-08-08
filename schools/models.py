from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import BaseModel


class School(BaseModel):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    address = models.CharField(max_length=255, blank=True, verbose_name=_('Address'))
    zipcode = models.CharField(max_length=10, blank=True, verbose_name=_('Zipcode'))
    phone = models.CharField(max_length=255, verbose_name=_('Phone'))
    website = models.CharField(max_length=255, blank=True, verbose_name=_('Website'))
    school_type = models.ForeignKey('SchoolType', on_delete=models.DO_NOTHING, verbose_name=_('School Type'))
    head_master = models.OneToOneField(get_user_model(), on_delete=models.CASCADE,
                                       related_name="school_head_master", verbose_name=_('Head Master'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('school')
        verbose_name_plural = _('schools')


class SchoolType(BaseModel):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    description = models.CharField(max_length=255, blank=True, verbose_name=_('Description'))

    def __str__(self):
        return self.name
