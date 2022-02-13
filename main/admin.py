from django.contrib import admin
from .models import *

class MateriaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Materia, MateriaAdmin)

class CursoAdmin(admin.ModelAdmin):
    pass
admin.site.register(Curso, CursoAdmin)

class AulaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Aula, AulaAdmin)

class EventoAdmin(admin.ModelAdmin):
    pass
admin.site.register(Evento, EventoAdmin)