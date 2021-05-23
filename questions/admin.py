from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Question

# To make pass read only


class QuestionAdmin(UserAdmin):
    list_display = ('userName', 'userSurname', 'title',
                    'description', 'isPublic', 'created_at')
    list_display_links = ('userName', 'userSurname', 'title')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Question, QuestionAdmin)
