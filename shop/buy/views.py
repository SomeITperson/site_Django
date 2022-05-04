from django.core.paginator import Paginator
from .utils import *
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import *
from .forms import *

class GoodsPage(ListView, DataMixin):
    paginate_by = 5
    model = Goods
    # goods_id = Goods.objects.values_list('id')
    # goods_name = Goods.objects.values_list('name')
    cats = Category.objects.all()
    template_name = 'buy/catalog.html'
    context_object_name = 'goods'
    extra_context = {'title' : 'Каталог', 'menu' : menu, 'cats' : cats, 'cat_selected' : 1, 'basket_selected' : 0}

    #Отображение только опубликованных записей
    def get_queryset(self):
        return Goods.objects.filter(is_published=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страницы")
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class GoodsPageCategory(ListView, DataMixin):
    model = Goods
    paginate_by = 20
    cats = Category.objects.all()
    template_name = 'buy/catalog.html'
    context_object_name = 'goods'
    extra_context = {'title' : 'Каталог', 'menu' : menu, 'cats' : cats}

    #Отображение только опубликованных записей
    def get_queryset(self):
        return Goods.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title=c.name)
        return dict(list(context.items()) + list(c_def.items()))


def main_page(request):
    session_key = request.session.session_key
    context = {
        'menu' : menu,
        'list' : list,
        'title' : 'Главная страница',
    }

    return render(request, 'buy/main.html', context=context)

# def catalog(request):
#     goods = Goods.objects.all()
#     cats = Category.objects.all()
#     context = {
#         'title': 'Каталог',
#         'menu': menu,
#         'goods' : goods,
#         'cats' : cats,
#     }
#     return render(request, 'buy/catalog.html', context=context)

def basket(request):
    goods = Goods.objects.all()
    #преобразование id элементов в список для отображения в корзине
    list = []
    if request.session.get('cart'):
        for item in request.session['cart']:
            list.append(int(item['id']))

    context = {
        'menu' : menu,
        'goods' : goods,
        'list' : list,
        'basket_selected' : 1,
        'cat_selected' : 0,
    }
    return render(request, 'buy/basket.html', context=context)

def about(request):
    goods = Goods.objects.all()
    cats = Category.objects.all()

    context = {
        'title' : 'О нас',
        'menu' : menu,
    }
    return render(request, 'buy/about.html', context=context)

#------------------------------------------------------------

def add_to_cart(request, id):
    if request.method == 'POST':
        if not request.session.get('cart'):
            request.session['cart'] = list()
        else:
            request.session['cart'] = list(request.session['cart'])

    # get list with ids
    # cart_ids_list = list()
    # for item in request.session['cart']:
    #     cart_ids_list.append(item['id'])

    item_exist = next((item for item in request.session["cart"] if item["type"] == request.POST.get("type") and item["id"] == id), False)

    add_data = {
        'type' : request.POST.get('type'),
        'id' : id,
    }

    if not item_exist:
        request.session['cart'].append(add_data)
        request.session.modified = True
    return redirect(f'http://127.0.0.1:8000/catalog/#{id}')

def remove_from_cart(request, id):
    goods = Goods.objects.all()
    # преобразование id элементов в список для отображения в корзине
    list = []
    if request.session.get('cart'):
        for item in request.session['cart']:
            list.append(int(item['id']))

    if request.method == 'POST':
        for item in request.session['cart']:
            if item['id'] == id:
                item.clear()

        while {} in request.session['cart']:
            request.session['cart'].remove({})

        if not request.session['cart']:
            del request.session['cart']

        request.session.modified = True

    return redirect(request.POST.get('url_from'))

def delete_cart(request):
    if request.session.get('cart'):
        del request.session['cart']
        request.session.modified = True
    return redirect(request.POST.get('url_from'))