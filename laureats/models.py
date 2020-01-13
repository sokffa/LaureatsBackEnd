from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]

class Profession(models.Model):
    id = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=255,blank=False,default='')
    class Meta:
        ordering = ['libelle']

class Filiere(models.Model):
    id = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=255,blank=False,default='')
    class Meta:
        ordering = ['libelle']

class Adresse(models.Model):
    id = models.AutoField(primary_key=True)
    pays = models.CharField(max_length=50,blank=False)
    ville = models.CharField(max_length=50,blank=True,default='')
    adresse = models.CharField(max_length=255,blank=True,default='')
    zip_code = models.IntegerField()
    class Meta:
        ordering = ['zip_code']

class Promotion(models.Model):
    id = models.AutoField(primary_key=True)
    annee_scolaire = models.IntegerField()
    class Meta:
        ordering = ['annee_scolaire']


def user_directory_path(instance, filename): 
   
    return 'static/images/user_{0}/{1}'.format(instance.cne, filename) 

class Laureat(models.Model):
    SITUATION_FAMILIALE = (
       (1, ('Célibataire')),
       (2, ('Marié(e)')),
   )
    cne = models.CharField(max_length=10, blank=False, default='',unique='True')
    nom = models.CharField(max_length=50, blank=False, default='')
    prenom = models.CharField(max_length=50, blank=False, default='')
    email = models.CharField(max_length=100, blank=True, default='',unique='True')
    telephone = models.CharField(max_length=12, blank=True, default='')
    pdp = models.ImageField(upload_to=user_directory_path,blank=True)
    situation_familiale = models.CharField(max_length=50, blank=False, default='' ,choices=SITUATION_FAMILIALE)
    nationalite = models.CharField(max_length=50, blank=False, default='')
    date_naissance = models.DateField()
    date_inscription = models.DateField()   
    sexe = models.CharField(max_length=50, blank=False, default='')
    promotion = models.ForeignKey(Promotion, on_delete = models.CASCADE, related_name="laureats") 
    adresse = models.ForeignKey(Adresse, on_delete = models.CASCADE, related_name="laureats") 
    filiere = models.ForeignKey(Filiere, on_delete = models.CASCADE, related_name="laureats") 
 
    class Meta:
        ordering = ['date_inscription']
    
class Etudiant(Laureat):
    etablissement = models.CharField(max_length=100, blank=False, default='')
    sujet_etude = models.CharField(max_length=255, blank=False, default='')
    new_date_inscription = models.DateField(blank=True,null=True)

    class Meta:
        ordering = ['new_date_inscription']
 
class Employe(Laureat):
    profession = models.ForeignKey(Profession, on_delete = models.CASCADE, related_name="employes") 
    date_debut = models.DateField()

    class Meta:
        ordering = ['date_debut']
