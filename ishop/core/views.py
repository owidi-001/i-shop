from django.shortcuts import render

# Create your views here.
def home(request):
    # context={'title':'Home page'}
    return render(request,'core/home.html')

def cart(request):
    # context={'title':'Home page'}
    return render(request,'core/home.html')