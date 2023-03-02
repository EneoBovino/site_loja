from django.db import models

class Category(models.Model):
    # As colunas de uma tabela são representadas por atributos da classe que representa a tabela.
    # Aqui foi definido uma coluna para armazenar o nome da categoria.
    # O nome é um campo de texto que possui um limite de caracteres que pode ser previamente definido.
    # Por isso usamos o tipo CharField e definimos seu limite em 150 caracteres.
    # O parâmetro verbose_name é responsável pelo nome que será exibido dentro do sistema web.
    # O nome da coluna dentro do banco de dados sempre será igual ao nome do atributo na classe.
    name = models.CharField(max_length=150, verbose_name="Nome")
    description = models.TextField(
        verbose_name="Descrição",
        # null=True,
        # blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"


class Color(models.Model):
    name = models.CharField(max_length=100, verbose_name="Cor")
    color_id = models.CharField(max_length=100, verbose_name="Código Cor")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Cor"
        verbose_name_plural = "Cores"

class Size(models.Model):
    name = models.CharField(max_length=50, verbose_name="Tamanho", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tamanho"
        verbose_name_plural = "Tamanhos"

class Brand(models.Model):
    name = models.CharField(max_length=150, verbose_name="Marca/Fabricante")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Marca/Fabricante"
        verbose_name_plural = "Marcas/Fabricantes"

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nome do Produto")
    description = models.TextField(verbose_name="Descrição do produto")
    price = models.FloatField(verbose_name="Preço")
    status = models.BooleanField(verbose_name="Disponível", default=True)
    stock = models.PositiveIntegerField(verbose_name="Estoque disponível")
    category = models.ForeignKey(Category, verbose_name="Categoria", on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, verbose_name="Marca/Fabricante", on_delete=models.CASCADE)
    color = models.ForeignKey(Color, verbose_name="Cor", on_delete=models.CASCADE)
    size = models.ForeignKey(Size, verbose_name="Tamanho", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
