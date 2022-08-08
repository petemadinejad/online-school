from django.contrib import admin
from .models import School


@admin.register(School)
class AuthorAdmin(admin.ModelAdmin):
    pass
