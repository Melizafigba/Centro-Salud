from django.db import models
from django.utils import timezone

# Create your models here.
class Paciente(models.Model):
    Creador = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    rut = models.CharField(max_length=9)
    Prevision = models.CharField(max_length=50)
    Especialidad = models.CharField(max_length=50)
    Region = models.CharField(max_length=30)
    Comuna = models.CharField(max_length=30)
    Centro_Medico = models.CharField(max_length=30)
    Fecha_de_Consulta = models.DateField(blank=True, null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.rut
