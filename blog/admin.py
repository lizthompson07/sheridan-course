"""Admin Setup"""

from django.contrib import admin

# Register your models here.

from . import models
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    """
    Set default admin view for Comment
    """
    list_display = (
        'name',
        'text',
        'approved',
        'created',
        'updated',
    )

    search_fields = (
        'text',
        'post__title',
        'name__username',
        'name__first_name',
        'name__last_name',
    )

    list_filter = (
        'approved',
        )


class CommentInline(admin.TabularInline):
    model = Comment
    fields = ('name', 'email', 'text', 'approved')
    readonly_fields = ('name', 'email', 'text', )
    extra = 0  # remove empty rows


class PostAdmin(admin.ModelAdmin):
    """
    Set default admin view in Django admin
    """
    ordering = ['created']

    list_display = (
        'title',
        # 'author',
        # 'status',
        'created',
        'updated',
    )

    search_fields = (
        'title',
        'author__username',
        'author__first_name',
        'author__last_name',
    )

    list_filter = (
        'status',
        'topics',
        )

    prepopulated_fields = {'slug': ('title',)}

    inlines = [
        CommentInline,
    ]


@admin.register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
    """
    Set default admin view for Topic
    """
    list_display = (
        'name',
        'slug',
    )

    prepopulated_fields = {'slug': ('name',)}


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Set default admin view for Contact
    """

    list_display = (
        'email',
        'last_name',
        'first_name',
        'submitted'
    )
    # Make these fields read-only in the admin
    readonly_fields = (
        'first_name',
        'last_name',
        'email',
        'message',
        'submitted'
    )


@admin.register(models.Contest)
class ContestAdmin(admin.ModelAdmin):
    """
    Set default admin view for Contact
    """
    ordering = ['-submitted']

    list_display = (
        'email',
        'last_name',
        'first_name',
        'submitted'
    )
    # Make these fields read-only in the admin
    readonly_fields = (
        'first_name',
        'last_name',
        'email',
        'photo',
        'submitted'
    )

    search_fields = (
        'first_name',
        'last_name',
        'email',
    )

admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Comment, CommentAdmin)

