from django.contrib import admin

from .models import Step

class StepAdmin(admin.ModelAdmin):
    ordering = ['step_number']

admin.site.register(Step, StepAdmin)
