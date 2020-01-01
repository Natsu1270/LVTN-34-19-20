from django.contrib import admin
from .models import Role


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_date')
    list_filter = ('name', 'is_active', 'created_date')
    list_display_links = ('name', 'description')
