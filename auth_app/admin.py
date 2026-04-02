from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from auth_app.models import AppUser

admin.site.register(AppUser, UserAdmin)
