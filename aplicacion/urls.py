from django.urls import path
from .views import home, contacto, galeria, agregar_producto, listar_productos, editar_producto, eliminar_producto

urlpatterns = [
    path('', home, name="home"),
    path('contacto', contacto, name="contacto"),
    path('galeria', galeria, name="galeria"),
    path("nuevo-producto/", agregar_producto, name="nuevo_producto"),
    path("listar-productos/", listar_productos, name="listar_producto"),
    path("modificar-producto/<id>/", editar_producto, name="editar_producto"),
    path("eliminar-producto/<id>/", eliminar_producto, name="eliminar_producto"),
]
