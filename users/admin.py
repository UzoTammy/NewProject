from django.contrib import admin
from .models import CustomUser as User
from django.contrib.auth.admin import UserAdmin


class UserAdminConfig(UserAdmin):
    ordering = ('-created_date',)
    search_fields = ('email', 'user_name', 'first_name')
    list_filter = ('email', 'user_name', 'first_name', 'is_staff')
    list_display = ('email', 'user_name', 'first_name', 'is_staff', 'is_active', 'modified_date')
    fieldsets = [
        (None, {'fields': ('email', 'user_name', 'created_date')}),
        ('Permission', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ( 'first_name', 'last_name',)})
    ]
    add_fieldsets = [
        (None, {'classes': ('wide',), 'fields': ('email', 'user_name', 'password1', 'password2', 'first_name', 'last_name')}),
        
    ]
                  
# Register your models here.
admin.site.register(User, UserAdminConfig)