from django.db import models
from softdelete.models import SoftDeleteModel
from produto.models import Produto

class Paletizacao(SoftDeleteModel):

    BLOCO_CHOICES = (
        ("A","A"), 
        ("B","B"),
        ("C","C"),
        ("D","D"),
        ("E","E"),
        ("F","F"),
        ("G","G"),
        ("H","H"),
        ("I","I"),
        ("J","J"),
    )
    RUAS_CHOICES = (
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
        ("5","5"),
        ("6","6"),
        ("7","7"),
        ("8","8"),
        ("9","9"),
        ("10","10"),
        ("11","11"),
        ("12","12"),
        ("13","13"),
        ("14","14"),
    )
    NIVEIS_CHOICES = (
        ("P","PICO"), 
        ("1","1"), 
        ("2","2"),
        ("3","3"), 
        ("4","4"),
        ("5","5"),
    )
    SEQUENCIA_CHOICES = (
        ("1","1"),
        ("2","2"),
    )

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    bloco = models.CharField(max_length=1, choices=BLOCO_CHOICES, blank=False, null=False)
    rua = models.CharField(max_length=2, choices=RUAS_CHOICES, blank=False, null=False)
    nivel = models.CharField(max_length=1, choices=NIVEIS_CHOICES, blank=False, null=False)
    sequencia = models.CharField(max_length=1, choices=SEQUENCIA_CHOICES, blank=False, null=False)

    class Meta:
        verbose_name = 'Paletização'
        verbose_name_plural = 'Paletizações'
        unique_together = ['bloco', 'rua', 'nivel', 'sequencia']

    def __str__(self):
        return f'{self.produto} em {self.bloco}R{self.rua}N{self.nivel}S{self.sequencia}'
