from django.contrib import admin
from .models import Paletizacao

class ManagePaletizacao(admin.ModelAdmin):
    list_display = ('produto', 'bloco', 'rua', 'nivel', 'sequencia')
    list_filter = ('produto', 'bloco', 'rua', 'nivel', 'sequencia', 'deleted_at')
    list_per_page = 20

admin.site.register(Paletizacao, ManagePaletizacao)