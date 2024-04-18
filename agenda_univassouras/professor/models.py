from django.contrib.auth.models import User
from django.db import models

class Professor(models.Model):
    matricula = models.IntegerField(primary_key=True)
    user = models.OneToOneField(User, related_name="professor", on_delete=models.CASCADE, null=True, blank=False)
    nome =  models.CharField(max_length=50, unique=False)

    def __str__(self):
        return '{0}'.format(self.nomeCompleto)





