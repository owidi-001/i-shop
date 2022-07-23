
from django import forms
from .models import User
from django.core.exceptions import ValidationError
from .validators import phone_number_validator, email_validator


class UserCreationForm(forms.ModelForm):
    email = forms.EmailField(help_text="Email is required")
    phone_number = forms.CharField(
        max_length=13, help_text="Phone number is required")
    username = forms.CharField(
        max_length=150, help_text="Username is required")
    is_vendor = forms.BooleanField(required=False, help_text="I want to be a vendor")

    class Meta:
        model = User
        fields = ["phone_number", "email", "username", "password", "is_vendor"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email:
            raise ValidationError("Please provide your email address")
        if not email_validator(email):
            raise ValidationError(
                "please provide a valid Email address")
        return email

    def clean_phone_number(self):
        phone_no = self.cleaned_data.get("phone_number")
        if not phone_no:
            raise ValidationError("please provide your phone number")
        if not phone_number_validator(phone_no):
            raise ValidationError(
                "please provide valid phone number eg +254712345678")
        return phone_no

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if not username:
            raise ValidationError("Username is required")
        return username

    def clean_is_vendor(self):
        is_vendor = self.cleaned_data.get("is_vendor")
        if not is_vendor:
            return False
        return True

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=150, widget=forms.PasswordInput)


class ResetPasswordForm(forms.Form):
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if not (password1 == password2):
            raise ValidationError("Passwords don't match")
        return password1


class UserAvatar(forms.Form):
    avatar = forms.ImageField(required=False)