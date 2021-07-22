from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages

from .forms import ContactForm


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(message, from_email, ['maisighie@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found!')
            messages.success(request, (
                "Thanks for getting in touch! "
                "We will respond to you as soon as possible."
            ))
            return redirect('home')

    context = {
        'form': form,
    }

    return render(request, 'contact/contact.html', context)
