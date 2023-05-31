from django.contrib import admin
from .models import Usuario, Especialidad, Rol, PersonalSalud, Horas, Ficha
admin.site.register(Usuario)
admin.site.register(Especialidad)
admin.site.register(Rol)
admin.site.register(PersonalSalud)
admin.site.register(Horas)
admin.site.register(Ficha)

