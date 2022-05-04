from .models import *
from django.db.models import Count

menu = [
    # {'title': 'О НАС', 'url_name': 'about'},
    {'title': 'КОРЗИНА', 'url_name': 'basket'},
    {'title': 'КАТАЛОГ', 'url_name': 'catalog'},
    {'title' : 'ГЛАВНАЯ', 'url_name' : 'main'},
]

class DataMixin():
    def get_user_context(self, **kwargs):
            context = kwargs
            cats = Category.objects.all()
            context['menu'] = menu
            context['cats'] = cats
            return context