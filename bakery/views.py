from django.shortcuts import render
from .models import Product,Category,Topcategory

# Create your views here.


def products(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    topcategorys = Topcategory.objects.all()
    return render(request, 'bak.html' , 
        {'products':products,
        'categories': categories,
        'topcategorys': topcategorys})