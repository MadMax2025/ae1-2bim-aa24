from django.contrib import admin

# Register your models here.
# importar las clases del modelo
from campeonatoNacional.models import Equipodefutbol
# agregar la clase Equipodefutbol para administrar
admin.site.register(Equipodefutbol)

