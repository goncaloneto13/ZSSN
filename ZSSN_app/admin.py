from django.contrib import admin
from ZSSN_app.models import Sobrevivente,Inventario


class Sobreviventes(admin.ModelAdmin):
    list_display = ('nome','id','inventario')
    list_display_links = ('nome','inventario')
    search_fields =('nome',)

admin.site.register(Sobrevivente, Sobreviventes)    

class Inventarios(admin.ModelAdmin):
    list_display = ('agua','alimentacao','medicacao','municao')

admin.site.register(Inventario,Inventarios)    

# Register your models here.
