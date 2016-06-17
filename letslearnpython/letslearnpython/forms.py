from django import forms

class ContactForm(forms.Form):
    message = forms.CharField(label='Your Message', widget=forms.Textarea, error_messages={'required': 'Please enter a message.'})
    name = forms.CharField(label='First Name', widget=forms.TextInput, error_messages={'required': 'Please enter your name.'})
    email = forms.CharField(label='Email', widget=forms.TextInput, error_messages={'required': 'Please enter your email address.'})
