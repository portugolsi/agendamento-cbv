from django.shortcuts import render,redirect
from .forms import AgendamentoForm
from .models import Agendamento
from django.db import IntegrityError
import os
from django.conf import settings
from django.contrib import messages
# Create your views here.

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

from googleapiclient.discovery import build
from datetime import datetime, timedelta

from datetime import datetime, timedelta
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar"]


def get_google_calendar_service():
    creds = None
    if os.path.exists(settings.GOOGLE_CREDENTIALS):
        creds = Credentials.from_authorized_user_file(settings.GOOGLE_CREDENTIALS)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(settings.GOOGLE_CREDENTIALS, ['https://www.googleapis.com/auth/calendar'])
            creds = flow.run_local_server(port=0)
        with open(settings.GOOGLE_CREDENTIALS, 'w') as token:
            token.write(creds.to_json())
    return build('calendar', 'v3', credentials=creds)


def create_google_calendar_event(summary, start_time, end_time, calendar_id, color_id):
    service = get_google_calendar_service()
    event = {
        'summary': summary,
        'start': {
            'dateTime': start_time.strftime('%Y-%m-%dT%H:%M:%S'),
            'timeZone': 'America/Sao_Paulo',
        },
        'end': {
            'dateTime': end_time.strftime('%Y-%m-%dT%H:%M:%S'),
            'timeZone': 'America/Sao_Paulo',
        },
        'color_id': color_id  # Definindo a cor do evento
    }
    event = service.events().insert(calendarId=calendar_id, body=event).execute()
    return event.get('id')

def converter_horario(horario):
    if horario == '1HORMAN':
        hora_inicio = datetime.strptime('07:00', '%H:%M').time()
        hora_fim = (datetime.strptime('07:00', '%H:%M') + timedelta(minutes=50)).time()
    elif horario == '2HORMAN':
        hora_inicio = datetime.strptime('07:50', '%H:%M').time()
        hora_fim = (datetime.strptime('07:50', '%H:%M') + timedelta(minutes=50)).time()
    elif horario == '3HORMAN':
        hora_inicio = datetime.strptime('08:40', '%H:%M').time()
        hora_fim = (datetime.strptime('08:40', '%H:%M') + timedelta(minutes=50)).time()
    elif horario == '4HORMAN':
        hora_inicio = datetime.strptime('10:00', '%H:%M').time()
        hora_fim = (datetime.strptime('10:00', '%H:%M') + timedelta(minutes=50)).time()
    elif horario == '5HORMAN':
        hora_inicio = datetime.strptime('10:50', '%H:%M').time()
        hora_fim = (datetime.strptime('10:50', '%H:%M') + timedelta(minutes=50)).time()
    elif horario == '6HORMAN':
        hora_inicio = datetime.strptime('11:40', '%H:%M').time()
        hora_fim = (datetime.strptime('11:40', '%H:%M') + timedelta(minutes=50)).time()
    else:
        # Adicione aqui tratamento de erro caso o valor de horário seja inválido
        hora_inicio = None
        hora_fim = None
    return hora_inicio, hora_fim


def index(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            novo_agendamento = form.save(commit=False)
            nova_data = novo_agendamento.data
            novo_horario = novo_agendamento.horario
            novo_laboratorio = novo_agendamento.laboratorio
            nome_professor = form.cleaned_data['professor']
            turma = form.cleaned_data['serie']
            # Converter o horário selecionado para hora inicial e final
            hora_inicio, hora_fim = converter_horario(novo_horario)

            # Combinar data e hora
            start_time = datetime.combine(nova_data, hora_inicio)
            end_time = datetime.combine(nova_data, hora_fim)

            # Criar evento no Google Calendar
            summary = f"Agendamento:{novo_laboratorio} - Prof. {nome_professor} | {turma}"
            calendar_id = 'c_7ad0b9c045e0a442e59e9027b79070848422e1261acc3cec9105d4ca16f53d35@group.calendar.google.com'
            color_id=''
            if novo_laboratorio=='Sala Google':
               
                color_id = '1' # '1' representa a cor azul
            
            elif novo_laboratorio=='Sala Microsoft':
                color_id = '2'
            
            elif novo_laboratorio=='Sala Hubb':
                color_id = '2'



            # Verificar se já existe um agendamento para o mesmo dia, horário e laboratório
            agendamentos_mesmo_horario = Agendamento.objects.filter(data=nova_data, horario=novo_horario, laboratorio=novo_laboratorio)

            if agendamentos_mesmo_horario.exists():
                messages.error(request, 'Já existe um agendamento para este dia, horário e laboratório.')
                return render(request, 'index.html', {'form': form, 'erro': 'Agendamento não realizado. Já existe um agendamento para este dia, horário ou laboratório.'})
            else:
                create_google_calendar_event(summary, start_time, end_time, calendar_id, color_id)

                messages.success(request, 'Agendamento realizado com Sucesso!')
                novo_agendamento.save()
                return render(request, 'index.html', {'form': form, 'success': 'Agendamento realizado com Sucesso!'})
    else:
        form = AgendamentoForm()
    return render(request, 'index.html', {'form': form})
