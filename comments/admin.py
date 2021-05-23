from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Comment

# To make pass read only


class CommentAdmin(UserAdmin):
    list_display = ('userName', 'userSurname', 'comment',
                    'questionId', 'projectId', 'created_at')
    list_display_links = ('userName', 'userSurname', 'comment')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Comment, CommentAdmin)
