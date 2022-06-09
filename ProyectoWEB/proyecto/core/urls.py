from xml.dom.minidom import Document
from django.conf import settings
from django.urls import URLPattern, path
from .views import home,quienesSomos,registro
from django.contrib.staticfiles.urls import static

urlpatterns=[
    path('',home,name="home"),
    path('quienesSomos',quienesSomos,name="quienesSomos"),
    path('registro',registro,name="registro"),
    path('Carrito',registro,name="Carrito"),
]