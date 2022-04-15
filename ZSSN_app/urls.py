from django.urls import path
from . import views
from ZSSN_app.api import viewsets as ZSSNviewsets


urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_sobreviventes, name='add_sobreviventes'),
    path('edit/<int:sobrevivente_pk>', views.edit_sobrevivente, name='edit_sobrevivente'),
    path('trocar_itens/<int:outro_pk>/<int:sobrevivente_pk>',views.trocar_itens, name='trocar_itens'),
    path('acusar/<int:sobrevivente_pk>/<int:acusado_pk>',views.acusar,name='acusar')
    
]
