from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Product
from profiles.models import UserProfile
from .forms import ReviewForm
from .models import Review



# Create your views here.

@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    user_profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review_title = form.cleaned_data['review_title']
            review_content = form.cleaned_data['review_content']
            review_rating = form.cleaned_data['review_rating']
            Review.objects.create(
                user_profile=user_profile,
                product=get_object_or_404(Product, pk=product_id),
                review_title=review_title,
                review_rating=review_rating,
                review_content=review_content)
            messages.success(request, 'Review added successfully.')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product review. \
                    Please check the form is valid and try again.')
    else:
        form = ReviewForm()
    template = 'reviews/add_review.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)
