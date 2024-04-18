from django.db import models
from professor.models import Professor

class Sala(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    qtd_computadores = models.IntegerField()
   
    def __str__(self):        
        return '{0}'.format(self.name)
    


class Turma(models.Model):
    nome = models.CharField(max_length=50)
    periodo = models.IntegerField()
    professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '{0} - {1}p'.format(self.nome, self.periodo)

class Agenda(models.Model):    
    titulo = models.CharField(max_length=255, unique=False)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, null=True)
    turma = models.ForeignKey(Turma, on_delete=models.SET_NULL, blank=True, null=True)
    date_init = models.DateTimeField(blank=False, null=True)
    date_end = models.DateTimeField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):        
        return "{0}".format(self.titulo)
    


    def duplicado(self):
        date_init = self.date_init
        date_end = self.date_end
        sala = self.sala        

        agendas = Agenda.objects.all()
        if(self.id != None):
            #NO CASO DE SE UPDATE EXCLUIR O PROPRIO ID
            agendas = agendas.exclude(id=self.id)
        agendamentos = (len(agendas\
            .filter(date_init__lte=date_init)\
            .filter(date_end__gte=date_init)\
            .filter(sala_id=sala.id))
            +
            len(agendas\
            .filter(date_init__lte=date_end)\
            .filter(date_end__gte=date_end)\
            .filter(sala_id=sala.id))           
            )
        return agendamentos

    def save(self, *args, **kwargs):                
        if(self.duplicado() > 0):                 
            raise ValueError('Sala já agendada nesse dia e horário!')
        else:
            super(Agenda, self).save(*args, **kwargs)