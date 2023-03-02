from django.urls import path
from produtos.views import index, produtos, produto

urlpatterns = [
    path('', index, name='index'),
    path('produtos', produtos, name='produtos'),
    path('produto/<int:product_id>', produto, name='produto')
]