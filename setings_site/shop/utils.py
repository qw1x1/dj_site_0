from .models import *
from django.db.models import Count
from django.core.cache import cache
from django.db.models import Sum


menu = [{'title': "О нас", 'url_name': 'home'},
        {'title': "Доставка", 'url_name': 'home'},
        {'title': "Способы оплаты", 'url_name': 'home'},
        {'title': "Корзина", 'url_name': 'cart'},
]

class DataMixin:
    paginate_by = 7

    def get_user_context(self, **kwargs):
        context = kwargs
        category = Category.objects.all()

        try:
            self.request.session['total_price'] = float(Product.objects.filter(available=True, slug__in=self.request.session.get('cart')).select_related('category').aggregate(Sum('price'))['price__sum'])
        except:
            self.request.session['total_price'] = str('0,00')
        
        context['menu'] = menu
        context['category'] = category
 
        return context