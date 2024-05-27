from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registro/', views.registro, name="registro"),
    path('listado/', views.listado, name='listado'),
    path('editar/<int:id>/', views.editar, name='editar'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('regauthper/<int:id>/', views.regauthper, name='regauthPer'),
    path('editar_authPer/<int:id>/', views.editar_authPer, name='editar_authPer'),
    path('save_edit_p/<int:id>/', views.save_edit_p, name='save_edit_p'),
    path('listadop/', views.listadoP, name='listadop'),
    path('regh/<int:id>/', views.regh, name='regH'),
    path('listadoh/', views.listadoH, name='listadoH'),
    path('edit_h/<int:id>/', views.edit_h, name='edit_h'),
    path('save_edit_h/<int:id>/', views.save_edit_h, name='save_edit_h'),    
    path('save_edit/<int:id>/', views.save_edit, name='save_edit'),
    path('datos/<int:id>/', views.datos, name='datos'),
    path('create_cred/<int:id>/', views.create_cred, name='create_cred'),
    path('create_sheet/<int:id>/', views.create_sheet, name='create_sheet'),
]
