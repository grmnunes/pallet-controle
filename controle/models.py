from django.db import models
from produto.models import Produto


class Controle(models.Model):
   
    TIPO_CHOICES = (
        ("E", "ENTRADA"),
        ("S", "SAIDA"),
    )
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES, blank=False, null=False)
    data = models.DateField(blank=False, null=False)
    quantidade = models.IntegerField(blank=False, null=False)
    observacoes = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    nota_fiscal = models.CharField(max_length=100, blank=True, null=True)
    

    def __str__(self):
        return self.produto.nome
