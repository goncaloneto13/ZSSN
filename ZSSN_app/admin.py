from django.contrib import admin
from jmespath import search
from ZSSN_app.models import Sobrevivente


class Sobreviventes(admin.ModelAdmin):
    list_display = ('Nome','Infectado','Log','Lat')
    list_display_links = ('Nome','Infectado')
    search_fields =('Nome',)

admin.site.register(Sobrevivente, Sobreviventes)    

# Register your models here.
