from django.contrib import admin

from .models import Laboratorio,Status,RecursosDidaticos,Agendamento

class AgendamentoAdmin(admin.ModelAdmin):
    # Define a ordem de classificação
    ordering = ['data']

admin.site.register(Laboratorio)
admin.site.register(Status) 
admin.site.register(RecursosDidaticos)
admin.site.register(Agendamento,AgendamentoAdmin)