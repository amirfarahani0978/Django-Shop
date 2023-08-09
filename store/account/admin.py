from typing import Any, Optional
from django.contrib import admin
from .forms import AccountChangeForm, AccountCreationForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import Account, OtpCode , Address

admin.site.register(Address)

@admin.register(OtpCode)
class OtpCodeAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'code', 'created')


class UserAdmin(BaseUserAdmin):
    form = AccountChangeForm
    add_form = AccountCreationForm
    list_display = ('phone_number', 'lastname', 'firstname', 'email',
                    'birth_date', 'gender', 'is_admin', 'is_active', 'last_login')
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
    readonly_fields = ('last_login',)
    # this method is used to disable the user if he is not superuser.

    def get_form(self, request: Any, obj: None,**kwargs: Any) -> Any:
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        if not is_superuser:
            form.base_fields['is_superuser'].disable = True
        return form


admin.site.register(Account, UserAdmin)
