from django.db import models

# Create your models here.
class filiere(models.Model):
    nom = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nom
    
class Projet(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    filiere = models.ForeignKey(filiere, on_delete=models.CASCADE)
    pdf = models.FileField(upload_to='projets/pdf/')
    image = models.ImageField(upload_to='projets/images/', null=True, blank=True)
    date_soumission = models.DateTimeField(auto_now_add=True)
    est_valide = models.BooleanField(default=False)
    
    def __str__(self):
        return self.titre