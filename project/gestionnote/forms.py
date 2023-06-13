from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
from django import forms

class examensForm(ModelForm):
    class Meta:
        model = models.examens
        fields = ('id','titre', 'date', 'coefficient')
        labels = {
            'id' : _('id'),
            'titre' : _('Titre'),
            'date' : _('date') ,
            'coefficient' : _('coefficient'),
        }    


class etudiantsForm(ModelForm):
    class Meta:
        model = models.etudiants
        fields = ('Netudiant','nom', 'prenom', 'groupe', 'photo', 'email')
        labels = {
            'Netudiant': _('Netudiant'),
            'nom': _('Nom'),
            'prenom': _('Prenom'),
            'groupe': _('Groupe'),
            'photo': _('Photo'),
            'email': _('Email')
        }

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class enseignantsForm(ModelForm):
    class Meta:
        model = models.Enseignant
        fields = ('id','nom', 'prenom')
        labels = {
            'id': _('id'),
            'nom' : _('nom'),
            'prenom' : _('prenom'),
        }       
        

 
class RuniteForm(ModelForm):
    class Meta:
        model = models.Runite
        fields = ['code_ressource','nom', 'descriptif', 'coefficient']
        labels = {
            'code_ressource': _('code_ressource'),
            'nom': _('Nom'),
            'descriptif': _('Descriptif'),
            'coefficient': _('Coefficient'),
        }
        
        
        
class UniteForm(ModelForm):
    class Meta:
        model = models.Unite
        fields = ['code','Nom', 'semestre', 'credit_ECTS']
        labels = {
            'code': _('code'),
            'Nom': _('Nom'),
            'semestre': _('semestre'),
            'credit_ECTS': _('credit ECTS'),

        }
            


class NoteForm(ModelForm):
    class Meta:
        model = models.Note
        fields = ('examen', 'etudiant', 'note', 'appreciation')
        labels = {
            'examen' : _('examen'),
            'etudiant' : _('etudiant'),
            'note' : _('note'),
            'appreciation' : _('appreciation'),
        }       
