from django.shortcuts import render,redirect
from django.contrib.auth import login

from django.contrib.auth.decorators import login_required
from .models import Vendor
from .forms import VendorForms


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
    return render(request,'vendors/vendors_admin.html',{'vendor':vendor})