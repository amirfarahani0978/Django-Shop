from django.contrib import admin
from .forms import AccountChangeForm, AccountCreationForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import Account, OtpCode


@admin.register(OtpCode)
class OtpCodeAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'code', 'created')


class UserAdmin(BaseUserAdmin):
    form = AccountChangeForm
    add_form = AccountCreationForm
    list_display = ('phone_number', 'lastname', 'firstname',)
    list_filter = ('lastname',)
    fieldsets = (
        (None, {'fields': ('phone_number', 'lastname', 'firstname',
         'email', 'image', 'postal_code', 'gender', 'birth_date',)}),
        ('permissions', {'fields': ('is_active', 'is_admin', 'is_superuser', 'last_login', 'groups', 'user_permissions')}
         ),
    )
    add_fieldsets = (
        (None, {'fields': ('phone_number', 'email',
         'firstname', 'lastname', 'password1', 'password2')}),
    )
    search_fields = ('phone_number', 'lastname')
    ordering = ('phone_number', 'lastname')
    filter_horizontal = ('groups', 'user_permissions')


admin.site.register(Account, UserAdmin)
