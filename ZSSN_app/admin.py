from django.contrib import admin
from jmespath import search
from ZSSN_app.models import Sobrevivente,Inventario


class Sobreviventes(admin.ModelAdmin):
    list_display = ('Nome','Infectado','Log','Lat')
    list_display_links = ('Nome','Infectado')
    search_fields =('Nome',)

admin.site.register(Sobrevivente, Sobreviventes)    

class Inventarios(admin.ModelAdmin):
    list_display = ('sobrevivente','agua','alimento','medicacao','municao')

admin.site.register(Inventario,Inventarios)    

# Register your models here.
