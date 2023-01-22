from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from .models import * # Импортируем модели
from .forms import * # Импортируем формы
from .utils import * # Импортируем миксины
from django.views.generic import ListView, DetailView, CreateView, FormView # Импортируем классы-представления
from django.contrib.auth.mixins import LoginRequiredMixin # Миксин для блокировки доступа не авторизованным пользователям 
from django.contrib.auth.views import LoginView 
from django.contrib.auth import logout, login

class SgopHome(DataMixin, ListView):
    model = Product # атрибут model ссылается на модель 
    template_name = 'shop/index.htm' # Передаём шаблон в представление
    # ListView - автоматически формирует колекцию object_list, с которой можно работать в teamplate, либо можем переопределить это имя 
    context_object_name = 'product' # теперь бкдем работать с колекцией по имени posts, имя используемое в templates

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs) # Берем ранее созданый контекст, чтобы не потерять его 
        # Обращаемся к методу миксина через self т.к он есть в нашем классе
        c_def = self.get_user_context(title='Главная страница') # Плюс передаем в kwargs(в наш контекст) -> title
        return dict(list(context.items()) + list(c_def.items())) # Объеденяем два наших контекста из ListView и DataMixin в один 

    # Для выборки данных оперделим метод get_queryset
    def get_queryset(self):
        # .select_related('cat') - жадная загруpка ForeignKey
        try:
            ordering = self.request.GET.get('orderby')
            return Product.objects.filter(available=True).select_related('category').order_by(ordering)
        except:
            return Product.objects.filter(available=True).select_related('category')

# Страница котрегории
class ProductCategory(DataMixin, ListView):
    model = Product # атрибут model ссылается на модель 
    template_name = 'shop/index.htm' # Передаём шаблон в представление
    # ListView - автоматически формирует колекцию object_list, с которой можно работать в teamplate, либо можем переопределить это имя 
    context_object_name = 'product'
    allow_empty = True


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs) # Сохраняем уже сформированный контекст
        # Через контекст обращаемся к posts, берём 1-ю запись и берем категорию, при этом в модели сработаем метод __str__ и вернём name
        c = Category.objects.get(slug=self.kwargs['category_slug'])
        c_def = self.get_user_context(title='Категория - ' + str(c.name))
        return dict(list(context.items()) + list(c_def.items()))

    # Для выборки данных оперделим метод get_queryset
    def get_queryset(self):
        # .select_related('cat') - жадная загруpка ForeignKey
        ordering = '-price'
        
        return Product.objects.filter(category__slug=self.kwargs['category_slug'], available=True).select_related('category')
    
    def get_ordering(self):
        ordering = self.request.GET.get('orderby')
        print(ordering)
        return ordering

# Страница отдельного товара
class ShowProduct(DataMixin, DetailView):
    model = Product
    template_name = 'shop/product.htm'
    slug_url_kwarg = 'product_slug' # Принудительно переопреденяем имя переменной из urls
    context_object_name = 'product' 
    allow_empty = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['product'])

        return dict(list(context.items()) + list(c_def.items()))

# Cart
class SgopCart(DataMixin, ListView):
    paginate_by = None
    model = Product # атрибут model ссылается на модель 
    template_name = 'cart/cart.htm' # Передаём шаблон в представление
    # ListView - автоматически формирует колекцию object_list, с которой можно работать в teamplate, либо можем переопределить это имя 
    context_object_name = 'product_in_cart' # теперь бкдем работать с колекцией по имени posts, имя используемое в templates
    allow_empty = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Ваша корзина") 
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        try:
            return Product.objects.filter(available=True, slug__in=self.request.session.get('cart')).select_related('category')
        except:
            return 0 


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'shop/register.htm'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация") 
        return dict(list(context.items()) + list(c_def.items())) 
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'shop/login.htm'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация") 
        return dict(list(context.items()) + list(c_def.items())) 

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
        logout(request)
        return redirect('login')