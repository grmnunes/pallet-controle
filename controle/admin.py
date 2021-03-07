from django.contrib import admin
from .models import Controle

class ManageControle(admin.ModelAdmin):
    list_display = ('tipo', 'produto', 'quantidade', 'data', 'nota_fiscal')
    list_filter = ('tipo', 'produto__nome', 'data', 'nota_fiscal' )
    list_per_page = 20


admin.site.register(Controle, ManageControle)
