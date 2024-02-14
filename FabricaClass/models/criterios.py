from django.db import models
class Criterios(models.Model):
   booleano = models.BooleanField()
   texto = models.TextField()
   numerico = models.IntegerField()

   def __str__(self):
     return self.all()