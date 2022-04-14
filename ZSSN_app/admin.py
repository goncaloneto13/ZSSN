from django.contrib import admin
from jmespath import search
from ZSSN_app.models import Sobrevivente,Item


class Sobreviventes(admin.ModelAdmin):
    list_display = ('Nome','Infectado','Log','Lat')
    list_display_links = ('Nome','Infectado')
    search_fields =('Nome',)

admin.site.register(Sobrevivente, Sobreviventes)    

class Itens(admin.ModelAdmin):
    list_display = ('nome','pontos')
admin.site.register(Item,Itens)


# Register your models here.
