import datetime

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from .forms import ContactForm

def index(request):
    context = {}
    return render(request, 'letslearnpython/index.html', context)

def contactus(request):
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sender = form.cleaned_data['email']
            sender_name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            from django.core.mail import send_mail
            email_dict = { 'sender': sender, 'sender_name': sender_name, 'message': message, 'date': datetime.date.today() }
            subject = "Contact message sent from austincs.org"
            body = render_to_string('letslearnpython/contact_notification.txt', email_dict)
            try:
                sent = send_mail(subject, body, settings.ADMINS[0][1], [settings.ADMINS[0][1]])
                context['success'] = True
                context['message'] = "Your message has been sent:" + "\n" + message
            except:
                context['success'] = False
                context['message'] = "Sorry, your message could not be sent at this time. Please try again later." + "\n" + message
    else:
        form = ContactForm()

    context['form'] = form

    return render(request, 'letslearnpython/contact.html', context)
