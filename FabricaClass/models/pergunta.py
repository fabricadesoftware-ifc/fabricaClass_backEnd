from django.db import models

class Pergunta(models.Model):
    criterio = models.ForeignKey("Criterios", on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.all()
