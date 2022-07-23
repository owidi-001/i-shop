from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify

from .models import Vendor
from .forms import VendorForms,ProductForm


# Create your views here.
def vendor(request):
    if request.method=="POST":
        form=VendorForms(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            vendor=Vendor.objects.create(name=user.username, created_by=user)
            return redirect('home')
    else:
        form=VendorForms()
    return render(request,'vendors/vendors.html',{'form':form})

@login_required
def vendor_admin(request):
    vendor=request.user.vendor
    products=vendor.products.all()
    return render(request,'vendors/vendors_admin.html',{'vendor':vendor},{'products':products})

# create product
@login_required
def add_product(request):
    if request.method=='POST':
        form=ProductForm(request.POST,request.FILES)

        if form.is_valid():
            product=form.save(commit=False)
            product.vendor=request.user.vendor
            product.slug=slugify(product.title)
            product.save()

            return redirect('vendor_admin')

    else:
        form =ProductForm()
    return render(request,'vendors/add_product.html',{'form':form})