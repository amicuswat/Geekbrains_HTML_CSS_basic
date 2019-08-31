from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'index.html')


def products(request):
    return render(request, 'products.html')


def contact(request):
    return render(request, 'contact.html')


# def test(request):
#     fruits = ['apple', 'banana', 'mango']
#     my_user = {
#         'first_name':'viktor',
#         'second_name':'Kuryshev'
#     }
#     return render(request, 'test.html', context={'fruits':fruits, 'my_user':my_user})