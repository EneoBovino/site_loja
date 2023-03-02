from django.shortcuts import render, get_object_or_404
from produtos.models import Product

# Create your views here.
def index(request):
    dados = Product.objects.all()

    return render(request, 'index.html', {"produtos":dados})

def produtos(request):
    dados = Product.objects.all()

    return render(request, 'produtos/produtos.html', {"data":dados})

def produto(request, product_id):
    produto_info = get_object_or_404(Product, pk=product_id)
    return render(request, 'produtos/produto.html', {"data":produto_info})