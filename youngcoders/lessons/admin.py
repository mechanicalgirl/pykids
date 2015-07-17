from django.contrib import admin

from .models import Lesson, Step

class LessonAdmin(admin.ModelAdmin):
    ordering = ['number']

class StepAdmin(admin.ModelAdmin):
    ordering = ['lesson', 'step_number']

admin.site.register(Lesson, LessonAdmin)
admin.site.register(Step, StepAdmin)
