from django.shortcuts import render

from apps.products.models import Product

# Create your views here.
def home(request):
    # context={'title':'Home page'}
    newest_products=Product.objects.all()[0:10]
    products=Product.objects.all()[10:]
    return render(request,'core/home.html',{'newest_products':newest_products},{'products':products})

def cart(request):
    # context={'title':'Home page'}
    return render(request,'core/home.html')