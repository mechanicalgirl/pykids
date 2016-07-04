from django.contrib import admin

from .models import Page

class PageAdmin(admin.ModelAdmin):
    ordering = ['page_name']

admin.site.register(Page, PageAdmin)
