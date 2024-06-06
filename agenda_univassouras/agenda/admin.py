from django.contrib import admin
from .models import Sala, Agenda, Turma

@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    ...

@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    ...

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    ...

    