from django.urls import path
from . import views

app_name = 'components'

urlpatterns = [
    path('', views.homepage, name='homePage'),
    path('contactus', views.contactus, name='contactPage'),
    path('about', views.aboutus, name='aboutPage'),
]
