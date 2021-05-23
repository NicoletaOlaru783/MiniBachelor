from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Project

# To make pass read only


class ProjectAdmin(UserAdmin):
    list_display = ('userName', 'userSurname', 'title',
                    'description', 'demoUrl', 'created_at')
    list_display_links = ('userName', 'userSurname', 'title')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Project, ProjectAdmin)
