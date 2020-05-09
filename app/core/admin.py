from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core import models


class UserAdmin(BaseUserAdmin):

    ordering = ['id']
    list_display =['email','name']

    # Need to edit cutom fields in the admin user page to support our custo model or it will give error unknown fields
    fieldsets = (# this is field sets class variable
          # Video show underscore but code did'nt run with underscore
          (None, {'fields': ('email', 'password')}),
          (('Personal Info'), {'fields': ('name',)}),
          (
             ('Permissions'),
             { 'fields': ('is_active', 'is_staff', 'is_superuser')}
          ),
          (('Important dates'), {'fields': ('last_login',)})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields' : ('email', 'password1', 'password2')
        }),
    )

admin.site.register(models.User, UserAdmin)
admin.site.register(models.Tag)
