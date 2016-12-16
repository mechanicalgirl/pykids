from django.shortcuts import render

def landing_page(request):
    """
    """

    return render(request, 'landing_app/landing_page.html')

def preview_landing_page(request):
    """
    """

    return render(request, 'landing_app/preview_landing_page.html')
