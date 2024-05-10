from django.urls import path, include

from . import views

urlpatterns = [
    path('registro/', views.registro, name="registro"),
    path('listado/', views.listado, name='listado'),
    path('editar/<int:id>/', views.editar, name='editar'),
    path('regauthper/<int:id>/', views.regauthper, name='regauthPer'),
    path('listadop/', views.listadoP, name='listadop'),
    path('regh/<int:id>/', views.regh, name='regH'),
    path('listadoh/', views.listadoH, name='listadoH'),
]
