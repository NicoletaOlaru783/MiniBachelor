from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

#To make pass read only
class AccountAdmin(UserAdmin):
    list_display = ('email', 'name', 'surname', 'role', 'school', 'programme', 'created_at')
    list_display_links = ('email', 'name', 'surname')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)


