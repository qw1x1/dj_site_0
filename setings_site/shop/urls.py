from django.urls import path
from .views import *



urlpatterns = [
    path('', SgopHome.as_view(), name='home'),
    path('category/<slug:category_slug>/', ProductCategory.as_view(), name='category'),
    path('product/<slug:product_slug>', ShowProduct.as_view(), name='product'),
    path('cart/', SgopCart.as_view(), name='cart'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
]

