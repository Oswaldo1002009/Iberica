from django.contrib import admin
from core.models import UserProfileInfo, User


@admin.register(UserProfileInfo)
class UserProfileInfoAdmin(admin.ModelAdmin):
    list_display = ['user', 'form_validate']
