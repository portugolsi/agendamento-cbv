from django import forms


from .models import Agendamento

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['professor', 'laboratorio','disciplina','serie','data','horario','proposta_da_aula','recursos_didaticos']
        labels = {
            'professor': 'Professor(a)',
            'recursos_didaticos':'Recursos didáticos (Pressione crtl para selecionar mais de um)',

        }
        widgets = {
            'professor': forms.TextInput(attrs={'placeholder': 'Digite o seu nome'}),
            'data': forms.DateInput(attrs={'placeholder': 'Selecione uma data', 'class': 'form-control'}),
            'disciplina': forms.TextInput(attrs={'placeholder': 'Informe a disciplina', 'class': 'form-control'}),
            'proposta_da_aula': forms.Textarea(attrs={'placeholder': 'Digite a proposta da aula', 'class': 'form-control'}),

        }