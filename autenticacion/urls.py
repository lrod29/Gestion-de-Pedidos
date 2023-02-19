from django.urls import path

from .views import Vregistro, cerrar_sesion


urlpatterns = [

    path('', Vregistro.as_view(), name="autenticacion"),
    path('cerrar_sesion', cerrar_sesion, name="cerrar_sesion"),
]
