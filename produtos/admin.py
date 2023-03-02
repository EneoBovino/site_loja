from django.contrib import admin

from produtos.models import Product, Category, Brand, Color, Size

# Register your models here.
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Size)

class ProductAdmin(admin.ModelAdmin):
    # Define quais os dados da tabela estarão disponíveis na tela de admin
    list_display = ('id', 'name', 'size', 'color', 'brand', 'price', 'stock', 'status')
    
    # Define quais dos dados mostrados permitirão o acesso aos dados do produto ao ser clicado
    list_display_links = ('id', 'name')

    # Define quais dados poderão ser editados diretamente pela lista
    list_editable = ('status', 'stock')

    # Define quais dados poderão ser filtrados através da exibição dos filtros na lista
    list_filter = ('size', 'color')

    # Define quantos items serão exibidos por página
    list_per_page = 10

    # Habilita a possibilidade de abrir um item para edição e salvar uma cópia como um novo produto
    save_as = True

    # Habilita a busca de items pelos campos definidos nesta tupla
    search_fields = ('name',)

admin.site.register(Product, ProductAdmin)

