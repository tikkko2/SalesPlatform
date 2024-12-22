from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    
    path('allproduct', views.products, name='products'),
    path('filtered_products', views.filtered_products, name='filteredProducts'),
    path('singleproduct/<int:id>', views.single_product, name='singleProduct'),
    path('women', views.women, name='women'),
    path('men', views.men, name='men'),
    path('kids', views.kids, name='kids'),

]