from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def services(request):
    return render(request,'services.html')

def photos(request):
    return render(request,'photos.html')

def contact(request):
    return render(request,'contact.html')

def quote(request):
    return render(request,'quote.html')