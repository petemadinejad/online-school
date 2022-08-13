from django.contrib import admin
from .models import School, SchoolType


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ["name", "phone", "address", "is_enable", "created_at"]
    list_filter = ["is_enable", "name"]
    search_fields = ["name"]


class SchoolInlineAdmin(admin.StackedInline):
    model = School
    fields = ["name", "address", "phone", "school_type", "head_master"]
    extra = 0


@admin.register(SchoolType)
class SchoolType(admin.ModelAdmin):
    list_display = ["name", "description", "is_enable", "created_at"]
    list_filter = ["is_enable"]
    search_fields = ["name"]
    inlines = [SchoolInlineAdmin]
