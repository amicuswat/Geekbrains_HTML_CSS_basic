from django.shortcuts import render

# Create your views here.
links_menu = [
    {'href': 'products_all', 'name': 'все'},
    {'href': 'products_home', 'name': 'дом'},
    {'href': 'products_office', 'name': 'офис'},
    {'href': 'products_modern', 'name': 'модерн'},
    {'href': 'products_classic', 'name': 'классика'},
]

links_main_menu = [
    {'href': 'main', 'name': 'Домой'},
    {'href': 'products_all', 'name': 'Продукты'},
    {'href': 'contact', 'name': 'Контакты'},
]


def main(request):
    context = {
        'title': 'Главная',
        'links_main_menu': links_main_menu,
    }
    return render(request, 'index.html', context=context)


def products(request):
    context = {
        'title': 'Продукты',
        'links_menu': links_menu,
        'links_main_menu': links_main_menu,
        # 'same_products':same_products
    }
    return render(request, 'products.html', context=context)


def contact(request):
    context = {
        'title': 'Контакты',
        'links_main_menu': links_main_menu,
    }
    return render(request, 'contact.html', context=context)

# def test(request):
#     fruits = ['apple', 'banana', 'mango']
#     my_user = {
#         'first_name':'viktor',
#         'second_name':'Kuryshev'
#     }
#     return render(request, 'test.html', context={'fruits':fruits, 'my_user':my_user})
