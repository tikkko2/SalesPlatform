from django.urls import path
from . import views

app_name = 'registration'

urlpatterns = [
    
    path('registration', views.registration, name='registration'),
    path('accountedit', views.account_edit, name='accountEdit'),
    path('login', views.login_page, name='loginPage'),
    path('logout', views.logout_page, name="logout"),
    path('cart', views.cart, name='cart'),
    path('addtocart/<int:id>', views.add_to_cart, name='addToCart'),
    path('removecart/<int:id>', views.delete_cart, name='deleteCart'),

]