from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from products.models import Product

class VendorForms(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model=User
        fields = ('username','email','password1','password2')


# product form
class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['category','image','title','description','price']