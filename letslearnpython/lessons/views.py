from django.shortcuts import render
from django.http import HttpResponse

from .models import Lesson, Step

def index(request):
    """Home page - list all lessons"""
    all_lessons = Lesson.objects.order_by('number')
    context = {
        'lesson_list': all_lessons,
    }
    return render(request, 'lessons/index.html', context)

def lesson_step(request, lesson_number, step_number):
    """A single step within a lesson"""
    lesson = Lesson.objects.get(number=lesson_number)
    step = Step.objects.get(lesson=lesson.id, step_number=step_number)
    all_steps = Step.objects.filter(lesson=lesson.id).order_by('step_number')

    prev_lesson = None
    try:
        prev_lesson = Lesson.objects.get(number=int(lesson_number)-1)
    except:
        pass

    next_lesson = None
    try:
        next_lesson = Lesson.objects.get(number=int(lesson_number)+1)
    except:
        pass

    context = {
        'lesson': lesson,
        'step': step,
        'step_list': all_steps,
        'prev_lesson': prev_lesson,
        'next_lesson': next_lesson,
    }
    return render(request, 'lessons/step.html', context)

def lesson(request, lesson_number):
    """All the steps within a single lesson"""
    lesson = Lesson.objects.get(number=lesson_number)
    all_steps = Step.objects.filter(lesson=lesson.id).order_by('step_number')

    prev_lesson = None
    try:
        prev_lesson = Lesson.objects.get(number=int(lesson_number)-1)
    except:
        pass

    next_lesson = None
    try:
        next_lesson = Lesson.objects.get(number=int(lesson_number)+1)
    except:
        pass

    context = {
        'lesson': lesson,
        'step_list': all_steps,
        'prev_lesson': prev_lesson,
        'next_lesson': next_lesson,
    }
    return render(request, 'lessons/lesson.html', context)
