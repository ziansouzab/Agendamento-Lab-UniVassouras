from django.db import models

class Sala(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    qtd_computadores = models.IntegerField()
   
    def __str__(self):        
        return '{0}'.format(self.name)
    
    
class Professor(models.Model):
    matricula = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=50, blank=False, unique=False)
    password = models.CharField(max_length=50, blank=False, null=False)
    email =  models.EmailField(unique=False)



class Agenda(models.Model):    
    titulo = models.CharField(max_length=255, blank=False, unique=False)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, blank=True, null=True)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, blank=False, null=True )
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
            raise ValueError('Sala já em uso nesse dia e horário.')
        else:
            super(Agenda, self).save(*args, **kwargs)