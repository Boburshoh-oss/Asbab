from django.urls import path
from django.urls import path,include
from . import views



urlpatterns = [
    path('product-grid/',views.products_grid, name='products_grid'),
]