from django.db import models


class Examens(models.Model):

    #id = models.models.IntegerField(primary_key = True)

    titre = models.CharField(max_length=100)
    date = models.DateField(max_length=10)
    coefficient = models.IntegerField(blank=False)

    def __str__(self):
        return f"{self.titre} écrit par {self.auteur} édité le {self.date}"

class Login(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)




class Enseignant(models.Model): #déclare la classe Livre héritant de la classe Model, classe de base des modèles
    
    #id = models.models.IntegerField(primary_key = True)

    nom = models.CharField(max_length=100) # défini un champs de type texte de 100 caractères maximum
    
    prénom = models.CharField(max_length = 100)
    
    
    def __str__(self):
        chaine = f"{self.titre}␣écrit␣par␣{self.auteur}␣édité␣le␣{self.date_parution}"
        return chaine





class Etudiant(models.Model): #déclare la classe Livre héritant de la classe Model, classe de base des modèles
    
    #Netudiant = models.models.IntegerField(primary_key = True)

    nom = models.CharField(max_length=100) # défini un champs de type texte de 100 caractères maximum
    
    prénom = models.CharField(max_length = 100)
    
    groupe = models.CharField(max_length = 5) # champs de type entier devant être obligatoirement rempli
    
    photo = models.ImageField(blank=True)
    
    email = models.EmailField(blank=False)
    #date_parution = models.DateField(blank=True, null = True) # champs de type date, pouvant être null ou ne pas être rempli
    #nombre_pages = models.IntegerField(blank=False) # champs de type entier devant être obligatoirement rempli
    #resume = models.TextField(null = True, blank = True) # champs de type text long
    def __str__(self):
        chaine = f"{self.nom}écrit␣par{self.prenom}édité␣le{self.email}"
        return chaine
    
    




class Runite(models.Model): #déclare la classe Livre héritant de la classe Model, classe de base des modèles
    
    #code_ressource = models.models.CharField(max_length=50, primary_key = True)

    nom = models.CharField(max_length=100) # défini un champs de type texte de 100 caractères maximum
    
    descriptif = models.CharField(max_length = 100)
    
    #!!!!!!!!!!!!!!! coefficient est un int 
    coefficient = models.IntegerField(blank=True, null = True) # champs de type date, pouvant être null ou ne pas être rempli
    
    # examen = models.models.ForeignKey("Examens.id", on_delete=models.CASCADE)

    def __str__(self):
        chaine = f"{self.titre}␣écrit␣par␣{self.auteur}␣édité␣le␣{self.date_parution}"
        return chaine







class Unite(models.Model): #déclare la classe Livre héritant de la classe Model, classe de base des modèles
    
    #code = models.models.CharField(max_length=50, primary_key = True)

    Nom = models.CharField(max_length=50) # défini un champs de type texte de 100 caractères maximum
    

    #semestre est un charfield
    semestre = models.IntegerField(max_length = 1)
    
    crédit_ECTS = models.IntegerField(blank=True, max_length= 3)
    def __str__(self):
        chaine = f"{self.titre}␣écrit␣par␣{self.auteur}␣édité␣le␣{self.date_parution}"
        return chaine
    





class Note(models.Model): #déclare la classe Livre héritant de la classe Model, classe de base des modèles
    
    #!!!!!!!!!!! note est un float et appreciation est un varchar(ou charfield)

    #examen est a changer par : examen = models.models.ForeignKey("Examens", on_delete=models.CASCADE)
    examens = models.CharField(max_length=50) # défini un champs de type texte de 100 caractères maximum
    
    #etudiant = models.models.ForeignKey("Etudiant.Netudiant", on_delete=models.CASCADE)
    etudiant = models.CharField(max_length = 50)
    
    note = models.IntegerField(blank=False, max_length = 4) # champs de type date, pouvant être null ou ne pas être rempli
    
    appréciation = models.CharField(blank=True, max_length=1000) # champs de type entier devant être obligatoirement rempli
    
    def __str__(self):
        chaine = f"{self.titre}␣écrit␣par␣{self.auteur}␣édité␣le␣{self.date_parution}"
        return chaine
