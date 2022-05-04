from django.urls import include, path
from .views import *


urlpatterns = [
    path('', main_page, name='main'),
    path('catalog/', GoodsPage.as_view(), name='catalog'),
    path('category/<slug:cat_slug>', GoodsPageCategory.as_view(), name='category'),
    #path('about/', about, name='about'),
    path('basket/', include([
            path('', basket, name='basket'),
            path('<id>/add/', add_to_cart, name='add'),
            path('<id>/remove', remove_from_cart, name='remove'),
            path('delete/', delete_cart, name='delete'),
        ]))
]