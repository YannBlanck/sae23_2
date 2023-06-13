from django.db import models


class examens(models.Model):

    id = models.models.IntegerField(primary_key = True)

    titre = models.CharField(max_length=100)
    date = models.DateField(max_length=10)
    coefficient = models.IntegerField(blank=False)

    def __str__(self):
        return f"{self.id} titre {self.titre} date {self.date} coefficient {self.coefficient}"

class Login(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)




class enseignants(models.Model): #déclare la classe Livre héritant de la classe Model, classe de base des modèles
    
    id = models.models.IntegerField(primary_key = True)

    nom = models.CharField(max_length=50) # défini un champs de type texte de 100 caractères maximum
    
    prenom = models.CharField(max_length = 50)
    
    
    def __str__(self):
        chaine = f"{self.id} nom {self.nom} prenom{self.prenom}"
        return chaine





class etudiants(models.Model): #déclare la classe Livre héritant de la classe Model, classe de base des modèles
    
    Netudiant = models.models.IntegerField(primary_key = True)

    nom = models.CharField(max_length=50) # défini un champs de type texte de 100 caractères maximum
    
    prenom = models.CharField(max_length = 50)
    
    groupe = models.CharField(max_length = 50) # champs de type entier devant être obligatoirement rempli
    
    photo = models.ImageField(blank=True)
    
    email = models.EmailField(blank=False)

    def __str__(self):
        chaine = f"{self.Netudiant} nom {self.nom}prenom{self.prenom} groupe {self.groupe} photo {self.photo} email {self.email}"
        return chaine
    
    




class Runite(models.Model): #déclare la classe Livre héritant de la classe Model, classe de base des modèles
    
    code_ressource = models.models.CharField(max_length=50, primary_key = True)

    nom = models.CharField(max_length=100) # défini un champs de type texte de 100 caractères maximum
    
    descriptif = models.CharField(max_length = 100)

    coefficient = models.IntegerField(blank=True, null = True)
    
    examen = models.models.ForeignKey("Examens.id", on_delete=models.CASCADE)

    def __str__(self):
        chaine = f"{self.code_ressource} nom {self.nom} descriptif {self.descriptif} coefficient {self.coefficient} examen {self.examen}"
        return chaine







class Unite(models.Model): #déclare la classe Livre héritant de la classe Model, classe de base des modèles
    
    code = models.models.CharField(max_length=50, primary_key = True)

    Nom = models.CharField(max_length=50) # défini un champs de type texte de 100 caractères maximum
    

    #semestre est un charfield
    semestre = models.CharField(max_length = 1)
    
    credit_ECTS = models.IntegerField(blank=True, max_length= 3)
    def __str__(self):
        chaine = f"{self.code} nom {self.Nom} semestre {self.semestre} credit_ECTS {self.credit_ECTS}"
        return chaine
    





class Note(models.Model): #déclare la classe Livre héritant de la classe Model, classe de base des modèles
    
    #!!!!!!!!!!! note est un float et appreciation est un varchar(ou charfield)

    #examen est a changer par : examen = models.models.ForeignKey("Examens", on_delete=models.CASCADE)
    examen = models.models.ForeignKey("Examens", on_delete=models.CASCADE)
    
    etudiant = models.models.ForeignKey("Etudiant.Netudiant", on_delete=models.CASCADE)
    #etudiant = models.CharField(max_length = 50)
    
    note = models.FloatField(blank=False, max_length = 4) # champs de type date, pouvant être null ou ne pas être rempli
    
    appreciation = models.CharField(blank=True, max_length=1000) # champs de type entier devant être obligatoirement rempli
    
    def __str__(self):
        chaine = f"{self.examen} etudiant {self.etudiant} note {self.note} appreciation {self.appreciation}"
        return chaine
