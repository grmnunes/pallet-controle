from django.db import models


class Produto(models.Model):
    TIPO_CHOICES = (
        ("F", "FARDO"),
        ("B", "BOBINA"),
        ("C", "CAIXA"),
        ("O", "OUTROS")
    )
    nome = models.CharField(max_length=150, unique=True)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES, blank=False, null=False)

    def __str__(self):
        return self.nome
