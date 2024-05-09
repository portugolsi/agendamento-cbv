from rest_framework import viewsets
from app.models import Agendamento
from app.api import serializers

class AgendamentoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AgendamentoSerializers# Linkando com o serializer que eu criei
    queryset = Agendamento.objects.all() #chamando todas tabelas que eu cr