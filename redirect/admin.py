from django.contrib import admin
from redirect.models import Page


class PageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'all',
        'android',
        'ios',
        'other',
    )

admin.site.register(Page, PageAdmin)
