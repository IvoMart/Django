from django.db import models
from django.db.models.fields import related

# Create your models here.
class Aeropuerto(models.Model):
  codigo = models.CharField( verbose_name=("COD"), max_length=3)
  ciudad = models.CharField( verbose_name=("Ciudad"), max_length=50)
  
  def __str__(self):
      return f'{self.codigo} ({self.ciudad})'

class Vuelo(models.Model):
  origen = models.ForeignKey( Aeropuerto , related_name=("Salidas"), on_delete=models.CASCADE)
  destino = models.ForeignKey( Aeropuerto , related_name=("Arribos"), on_delete=models.CASCADE)
  duracionV = models.FloatField(("Tiempo"))
  
  def __str__(self):
      return f'{self.id}: Desde {self.origen} a {self.destino}. Tiempo: {self.duracionV}'
