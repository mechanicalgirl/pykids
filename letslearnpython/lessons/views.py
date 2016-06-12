from django.shortcuts import render
from django.http import HttpResponse

from .models import Lesson, Step

def index(request):
    """Home page - list all lessons"""
    all_lessons = Lesson.objects.order_by('number')
    context = {
        'lesson_list': all_lessons,
    }
    return render(request, 'lessons/step.html', context)

def lesson_step(request, lesson_number, step_number):
    """A single step within a lesson"""

    all_lessons = Lesson.objects.order_by('number')
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
        
    prev_step = None
    try:
        prev_step = Step.objects.get(lesson=lesson.id, step_number=int(step_number)-1)
    except:
        # If this is the first step in this lesson, the "previous" step is
        # the last step of the previous lesson.
        if prev_lesson:
            try:
                prev_step = Step.objects.filter(lesson=prev_lesson.id).order_by('-step_number')[0]
            except:
                pass

    next_step = None
    try:
        next_step = Step.objects.get(lesson=lesson.id, step_number=int(step_number)+1)
    except:
        # If this is the last step in this lesson, the "next" step is the
        # first step of the next lesson.
        if next_lesson:
            try:
                next_step = Step.objects.get(lesson=next_lesson.id, step_number=1)
            except:
                pass
        
    context = {
        'lesson': lesson,
        'lesson_list': all_lessons,
        'step': step,
        'step_list': all_steps,
        'prev_lesson': prev_lesson,
        'next_lesson': next_lesson,
        'prev_step': prev_step,
        'next_step': next_step,
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
