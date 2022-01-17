from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CasinoUser

class UserAdminConfig(UserAdmin):
    ''' Customized User Management Dasboard for Admin '''
    model = CasinoUser
    search_fields = ('email', 'user_name', 'first_name',)
    list_filter = ('email', 'user_name', 'first_name', 'balance', 'is_active', 'is_staff')
    ordering = ('user_name',)
    list_display = ('email', 'user_name', 'first_name', 'balance', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name', 'balance')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('last_name',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'last_name', 'balance', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )

admin.site.register(CasinoUser, UserAdminConfig)