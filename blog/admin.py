from django.contrib import admin

# Register your models here.

from . import models


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'created',
        'updated',
    )


admin.site.register(models.Post, PostAdmin)
