from django.db import models

class Laboratorio(models.Model):
    nome = models.CharField(max_length=30)

    class Meta: #Definindo o nome da classe no plural
        verbose_name_plural = "Laboratorios"
    def __str__(self):
        return self.nome

class Status(models.Model):
    desc = models.CharField(max_length=30,default='Não Agendado')

    class Meta: #Definindo o nome da classe no plural
        verbose_name_plural = "Status"
    def __str__(self):
        return self.desc

class RecursosDidaticos(models.Model):
    nome = models.CharField(max_length=30)
    class Meta: #Definindo o nome da classe no plural
        verbose_name_plural = "Recursos didáticos"
    def __str__(self):
        return self.nome

class Agendamento(models.Model):
    SERIES_CHOICES = [
        ('1ANO','1 ANO'),
        ('2ANO','2 ANO'),
        ('3ANO','3 ANO'),
        ('4ANO','4 ANO'),
        ('5ANO','5 ANO'),
        ('6ANO','6 ANO'),
        ('7ANO','7 ANO'),
        ('8ANO','8 ANO'),
        ('9ANO','9 ANO'),
        ('1SERIE','1 SÉRIE'),
        ('2SERIE','2 SÉRIE'),
        ('3SERIE','3 SÉRIE')
        ]
    
    HORARIOS_CHOICES = [
            ('1HORMAN','07:00 às 07:50'),
            ('2HORMAN','07:50 às 08:40'),
            ('3HORMAN','08:40 às 09:30'),
            ('4HORMAN','10:00 às 10:50'),
            ('5HORMAN','10:50 às 11:40'),
            ('6HORMAN','11:40 às 12:30'),    
        ]
    professor = models.CharField(max_length=150)
    laboratorio = models.ForeignKey(Laboratorio,on_delete=models.CASCADE)
    disciplina = models.CharField(max_length=30)
    serie = models.CharField(choices=SERIES_CHOICES,max_length=30)
    data = models.DateField()
    horario = models.CharField(choices=HORARIOS_CHOICES,max_length=150)
    proposta_da_aula = models.TextField()
    recursos_didaticos = models.ManyToManyField(RecursosDidaticos)
    status = models.ForeignKey(Status,on_delete=models.CASCADE,default=2)


    class Meta: #Definindo o nome da classe no plural
        verbose_name_plural = "Agendamentos"
    def __str__(self):
        return  str(self.data.day) + "/" + str(self.data.month)+ " | " + self.professor   +" no laboratorio " + self.laboratorio.nome + " às " + self.horario 

