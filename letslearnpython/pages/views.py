from django.http import HttpResponse
from django.shortcuts import render

from .models import Page

def index(request, page_name):
    page = Page.objects.get(page_name=page_name)
    context = {
        'page': page,
    }
    return render(request, 'pages/page.html', context)
