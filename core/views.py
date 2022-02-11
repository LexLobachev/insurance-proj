from django.db.models import Q
from django.shortcuts import render
from product.models import Product


def homepage(request):
    newest_products = []
    query = request.GET.get('query')
    if query is None:
        newest_products = Product.objects.all()[0:8]
    else:
        newest_products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query)
                                      | Q(interest_rate__icontains=query) | Q(category__icontains=query))
    return render(request, 'core/home.html', {'newest_products': newest_products, 'query': query})
