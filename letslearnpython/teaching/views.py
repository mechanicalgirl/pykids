from django.http import HttpResponse
from django.shortcuts import render

from .models import Step

def index(request):
    """Home page - list all organizer steps"""
    all_steps = Step.objects.order_by('step_number')
    context = {
        'step_list': all_steps,
    }
    return render(request, 'teaching/step.html', context)

def step(request, step_number):
    step = Step.objects.get(step_number=step_number)
    all_steps = Step.objects.all().order_by('step_number')
    context = {
        'step': step,
        'step_list': all_steps,
    }
    return render(request, 'teaching/step.html', context)
