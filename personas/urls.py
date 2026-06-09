from django.urls import path

from . import views

urlpatterns = [
    path('', views.llamar_incio, name = 'inicio'),
    path('contacto/', views.llamar_contacto, name= 'contacto'),
    path('listaP/', views.lista_personas, name='listaP'),
    path('listar-personas/', views.ListEmpleadosPdf.as_view(),name='personas_all')
]
