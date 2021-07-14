from django.shortcuts import render
from products.models import Product


def index(request):

    products = Product.objects.order_by('name').all()[:4]
    context = {
        'products': products,
    }

    return render(request, 'home/index.html', context)
