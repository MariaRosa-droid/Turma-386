from django.db import models

# Create your models here.
class  Pedido(models . Model):
    tipo_categoria = models.CharField(max_length=50)
    descricao = models.CharField(max_length = 80)
    qtdPrevistoMes = models.FloatField ()
    preco = models.FloatField ()
    precoMaximo = models.FloatField ()

    def __str__(self):
        return self.tipo_categoria
