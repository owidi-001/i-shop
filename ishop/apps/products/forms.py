from django import forms

class AddToCartForm(forms.Form):
    """AddTocart definition."""

    quantity=forms.IntegerField()
