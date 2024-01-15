from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import VrUser

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'mobile_number', 'is_Vruser', 'is_admin', 'is_staff', 'is_customer', 'is_active','is_seller')
    search_fields = ('email', 'first_name', 'last_name', 'mobile_number')
    list_filter = ('is_Vruser', 'is_admin', 'is_staff', 'is_customer', 'is_active')

admin.site.register(VrUser, CustomUserAdmin)
