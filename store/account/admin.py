from django.contrib import admin
from .forms import AccountChangeForm, AccountCreationForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import Account


class UserAdmin(BaseUserAdmin):
    form = AccountChangeForm
    add_form = AccountCreationForm
    list_display = ('phone_number', 'lastname', 'firstname',)
    list_filter = ('lastname',)
    fieldsets = (
        (None, {'fields': ('phone_number', 'lastname', 'firstname')}),
         ('permissions', {'fields': ('is_active', 'is_admin', 'last_login')}
         ),
    )
    add_fieldsets = (
        (None, {'fields': ('phone_number', 'email', 'firstname','lastname', 'password1', 'password2')}),
    )
    search_fields = ('phone_number', 'lastname')
    ordering = ('phone_number', 'lastname')
    filter_horizontal = ()


admin.site.unregister(Group)
admin.site.register(Account, UserAdmin)
