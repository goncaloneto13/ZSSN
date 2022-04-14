from django.urls import path
from . import views
from ZSSN_app.api import viewsets as ZSSNviewsets



urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_sobreviventes, name='add_sobreviventes'),
    path('edit/<int:sobrevivente_pk>', views.edit_sobrevivente, name='edit_sobrevivente')
    
]
