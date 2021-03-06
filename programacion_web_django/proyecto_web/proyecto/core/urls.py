from xml.dom.minidom import Document
from django.conf import settings
from django.urls import URLPattern, path
from .views import home,quienesSomos,registro,tienda,iniciarSesion,tienda2,carrito
from django.contrib.staticfiles.urls import static

urlpatterns=[
    path('',home,name="home"),
    path('quienesSomos/',quienesSomos,name="quienesSomos"),
    path('registro/',registro,name="registro"),
    path('tienda/',tienda,name="tienda"),
    path('iniciar_sesion/<id>',iniciarSesion,name="iniciarSesion"),
    path('tienda2/',tienda2,name="tienda2"),
    path('carrito/',carrito,name='carrito'),
]