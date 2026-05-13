from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('produk/', views.produk, name='produk'),
    path('produk/<int:id>/', views.detail_produk, name='detail_produk'),
    path('kontak/', views.kontak, name='kontak'),
]