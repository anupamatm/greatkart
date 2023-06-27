from django.shortcuts import get_object_or_404, render

from category.models import Category

from .models import Product

# Create your views here.

def store(request, category_slug = None):
    categories=None
    products=None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products= Product.objects.filter(is_available=True,category=categories)
        product_count= products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()
        categories = Category.objects.all()

    context = {
        'products':products,
        'categories':categories,
        'product_count':product_count
    }
    return render(request,'store/store.html',context)


def product_deatail(requst, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug = category_slug, slug = product_slug)
    except Exception as e:
        raise e
    
    context={
        'single_product':single_product
    }
    return render(requst, 'store/product_deatail.html',context)