from django.contrib import admin
from django.conf import settings
from .models import User


admin.site.site_header = settings.PROJECT_NAME + ' admin'


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'email')
    exclude = ('groups', 'user_permissions', 'email_hash')
    search_fields = ('username', 'first_name', 'email')

