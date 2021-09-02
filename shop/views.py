from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    products = Product.objects.all()

    #search Items Code
    query = request.GET.get('query')
    if query != '' and query is not None: 
        products = Product.objects.filter(title__icontains=query) 

    #Pagination Code
    paginator = Paginator(products, 4)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    # Content To Pass
    context = {
        'products': products
    }
    return render(request, 'shop/index.html', context)


def detail(request,id):
    product = Product.objects.get(id=id)
    
    context = {
        'product': product
    }
    return render(request, 'shop/detail.html', context)


