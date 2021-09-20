import random

from django.contrib import messages
from django.shortcuts import redirect, render,get_object_or_404
from django.db.models import Q

from .forms import AddToCartForm
from .models import Category, Product


from apps.cart.cart import Cart
# Create your views here.


def product(request,category_slug,product_slug):
    cart=Cart(request)
    product=get_object_or_404(Product,category_slug=category_slug,slug=product_slug)

    if request.method=='POST':
        form =AddToCartForm(request.POST)

        if form.is_valid():
            quantity=form.cleaned_data['quantity']

            cart.add(product_id=product.id,quantity=quantity,update_quantity=False)

            messages.success(request,'The product was added to the cart')

            return redirect('product',category_slug=category_slug,product_slug=product_slug)
    similar_products=list(product.category.products.exclude(id=product.id))

    if len(similar_products >=4):
        similar_products=random.sample(similar_products,4)
    return render(request,'products/product.html',{'product':product,'similar_products':similar_products})


# category view
def category(request,category_slug):
    category=get_object_or_404(Category,slug=category_slug)
    return render(request,'products/category',{'category':category})


# search 
def search(request):
    query=request.GET.get('query','')
    print(query)
    products=Product.objects.filter(Q(title_icontains=query) | Q(description_icontains=query))
    return render(request,'products/search.html',{'products':products,'query':query})