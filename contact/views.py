from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .forms import ContactForm


def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        customer_query = request.POST.get('message')
        customer_email = request.POST.get('email')
        customer_name = request.POST.get('full_name')
        if form.is_valid():
            form.save()

            send_mail(
                'Maisigh.ie - New Contact Form',
                'A new email has been received from:'
                f'\n\n{customer_name}'
                f'\n{customer_email}'
                '\n\n\nCustomer Query:'
                f'\n\n{customer_query}',
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],
            )

            messages.success(request, 'Email sent. We will be in touch soon!')
            return redirect(reverse('home'))
        else:
            messages.error(
                request,
                'Contact request failed. Check the form is valid')
    else:
        form = ContactForm()

    context = {
        'form': form
    }

    return render(request, 'contact/contact.html', context)
