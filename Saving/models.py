from django.db import models

# Create your models here.

class Saving(models.Model):
    DEPOT = 'DEPOT'
    RETRAIT = 'RETRAIT'

    TYPE_CHOICES = [
        (DEPOT, 'Dépôt'),
        (RETRAIT, 'Retrait'),
    ]
    
    type_operation = models.CharField(max_length=10, choices=TYPE_CHOICES, default=DEPOT, verbose_name="Type d'opération")
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    motif = models.TextField()
    date_ajout = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.type_operation} de {self.montant} FCFA"



class SoldeGlobal(models.Model):
    montant_total = models.DecimalField(max_digits=15, decimal_places=0, default=0)

    def __str__(self):
        return f"Solde actuel : {self.montant_total} FCFA"



