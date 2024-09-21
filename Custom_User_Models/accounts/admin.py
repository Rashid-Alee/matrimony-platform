from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = [
        "username",
        "email",
    ]
    search_fields = [
        "username",
    ]


admin.site.register(CustomUser, CustomUserAdmin)
# Register your models here.
