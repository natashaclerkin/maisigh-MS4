from django.http import HttpResponse
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import ContactForm

# Create your views here.


def contact(request):
    """ Customer contact form view """
    contact_form = ContactForm
    if request.method == "POST":
        form = contact_form(data=request.POST)

        if form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            message = request.POST.get('message', '')

        send_mail(
            name,
            message,
            email,
            [settings.DEFAULT_FROM_EMAIL]
        )
        return redirect('contact')
    context = {
        'form': contact_form,
        }

    return render(request, 'contact/contact.html', context)
