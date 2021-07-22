from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .forms import ContactForm


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            messages.success(request, (
                "Thanks for getting in touch! "
                "The Maisigh crew will get back to you shortly."
            ))
        return redirect('home')

    context = {
        'form': form,
    }

    return render(request, 'contact/contact.html', context)
