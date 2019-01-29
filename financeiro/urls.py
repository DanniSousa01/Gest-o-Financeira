from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('usuarios/', views.usuario_list),
    path('usuarios/<int:usuario_id>/', views.usuario_show),
    path('despesas/', views.despesa_list),
    path('despesas/<int:despesa_id>/', views.despesa_show)
]