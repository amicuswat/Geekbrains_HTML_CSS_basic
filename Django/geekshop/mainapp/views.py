from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'index.html')


def products(request):
    return render(request, 'products.html')


def contact(request):
    return render(request, 'contact.html')
