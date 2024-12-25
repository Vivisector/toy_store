from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('store/', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('register/', views.register, name='register'),
    path('news/', views.news_list, name='news'),
]
