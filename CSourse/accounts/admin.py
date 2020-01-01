from django.contrib import admin
from .models import User, Profile
from django.conf import settings


admin.site.site_header = settings.PROJECT_NAME + ' admin'


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'email')
    exclude = ('groups', 'user_permissions', 'email_hash')
    search_fields = ('username', 'first_name', 'email')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'gender', 'phone_number')
