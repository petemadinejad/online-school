from django.db import models
from django.contrib.auth import get_user_model
from base.models import BaseModel


class School(BaseModel):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True)
    zipcode = models.CharField(max_length=10, blank=True)
    phone = models.CharField(max_length=255)
    website = models.CharField(max_length=255, blank=True)
    school_type = models.ForeignKey('SchoolType', on_delete=models.DO_NOTHING)
    head_master = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name="school_head_master", )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'school'
        verbose_name_plural = 'schools'


class SchoolType(models.TextChoices):
    pass