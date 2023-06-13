from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import examensForm , LoginForm , etudiantsForm , RuniteForm, UniteForm, NoteForm , enseignantsForm
from . import models
from django.shortcuts import get_object_or_404



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username == 'toto' and password == 'toto':
            
            return redirect('/gestionnote/ajout/')
        
        if username == 'prof' and password == 'prof':

            return redirect('/gestionnote/ajout/')
        
        error_message = "Invalid username or password."
        return render(request, 'gestionnote/login.html', {'error_message': error_message})
    
    return render(request, 'gestionnote/login.html')


def main(request):
    return render(request, 'gestionnote/main.html')



def login(request):
    return render(request, 'gestionnote/login.html')



def ajout(request):
    
        form = examensForm()
        return render(request, 'gestionnote/ajout.html', {'form': form})


def traitement(request):
    lform = examensForm(request.POST)
    if lform.is_valid():
        examens = lform.save()
        return render(request, 'gestionnote/affiche.html', {'examens': examens})
        #return HttpResponseRedirect("/gestionnote/all/")
    else:
        return render(request, 'gestionnote/ajout.html', {'form': lform})
    
    
def all(request):
    examenss = list(models.examens.objects.all())
    etudiants = list(models.etudiants.objects.all())
    return render(request, 'gestionnote/all.html', {'examenss': examenss,'etudiant': etudiants})
    


def read(request,id):
    examens = models.examens.objects.get(pk=id)
    return render(request, 'gestionnote/affiche.html', {'examens': examens})

def traitementupdate(request, id):
    lform = examensForm(request.POST)
    if lform.is_valid():
        
        examens = lform.save(commit=False)
        examens.id = id
        examens.save()
        return HttpResponseRedirect("/gestionnote/all/")
    else:
        return render(request, 'gestionnote/update.html', {'form': lform, 'id': id})
        
    return HttpResponse("ok") 


def update(request, id):
    examens = get_object_or_404(models.examens, pk=id)
    form = examensForm(instance=examens)
    """
    if request.method == 'POST':
        form = LivreForm(instance=livre)
        if form.is_valid():
            form.save()
            return redirect('nom-de-la-page')
    """
    return render(request, 'gestionnote/update.html', {'form': form, 'id': id})

def delete(request, id):
    examens = get_object_or_404(models.examens, pk=id)
    examens.delete()
    return HttpResponseRedirect("/gestionnote/all/")





def ajoutenseignant(request):
    if request.method == "POST":
        
        form = enseignantsForm(request)
        if form.is_valid():
            enseignant = form.save()
            return render(request, 'gestionnote/affiche.html', {'enseignant': enseignant})
        else:
            return render(request, 'gestionnote/ajoutenseignant.html', {'form': form})
    else:
        form = enseignantsForm()
        return render(request, 'gestionnote/ajoutenseignant.html', {'form': form})


def traitementenseignant(request):
    lform = enseignantsForm(request.POST)
    if lform.is_valid():
        enseignant = lform.save()
        return render(request, 'gestionnote/affiche.html', {'enseignant': enseignant})
    else:
        return render(request, 'gestionnote/ajoutenseignant.html', {'form': lform})
    
    
def allenseignant(request):
    enseignants = list(models.enseignants.objects.all())
    return render(request, 'gestionnote/all.html', {'enseignants': enseignants})


def readenseignant(request,id):
    enseignant = models.enseignants.objects.get(pk=id)
    return render(request, 'gestionnote/affiche.html', {'enseignant': enseignant})

def traitementupdateenseignant(request, id):
    lform = enseignantsForm(request.POST)
    if lform.is_valid():
        
        enseignant = lform.save(commit=False)
        enseignant.id = id
        enseignant.save()
        return HttpResponseRedirect("/gestionnote/all/")
    else:
        return render(request, 'gestionnote/update.html', {'form': lform, 'id': id})
        
    return HttpResponse("ok") 


def updateenseignant(request, id):
    enseignant = get_object_or_404(models.enseignants, pk=id)
    form = enseignantsForm(instance=enseignant)
    """
    if request.method == 'POST':
        form = LivreForm(instance=livre)
        if form.is_valid():
            form.save()
            return redirect('nom-de-la-page')
    """
    return render(request, 'gestionnote/update.html', {'form': form, 'id': id})

def deleteenseignant(request, id):
    enseignant = get_object_or_404(models.enseignant, pk=id)
    enseignant.delete()
    return HttpResponseRedirect("/gestionnote/all/")






 
def ajoutetudiant(request):
    if request.method == "POST":
        
        form = etudiantsForm(request)
        if form.is_valid():
            etudiant = form.save()
            return render(request, 'gestionnote/afficheetudiant.html', {'etudiant': etudiant})
        else:
            return render(request, 'gestionnote/ajoutetudiant.html', {'form': form})
    else:
        form = etudiantsForm()
        return render(request, 'gestionnote/ajoutetudiant.html', {'form': form})


def traitementetudiant(request):
    lform = etudiantsForm(request.POST)
    if lform.is_valid():
        etudiant = lform.save()
        return render(request, 'gestionnote/afficheetudiant.html', {'etudiant': etudiant})
    else:
        return render(request, 'gestionnote/ajoutetudiant.html', {'form': lform})
    
def alletudiant(request):
    etudiants = list(models.etudiants.objects.all())
    return render(request, 'gestionnote/all.html', {'etudiants': etudiants})


def readetudiant(request,id):
    etudiant = models.etudiants.objects.get(pk=id)
    return render(request, 'gestionnote/afficheetudiant.html', {'etudiant': etudiant})

def traitementupdateetudiant(request, id):
    lform = etudiantsForm(request.POST)
    if lform.is_valid():
        
        etudiant = lform.save(commit=False)
        etudiant.id = id
        etudiant.save()
        return HttpResponseRedirect("/gestionnote/all/")
    else:
        return render(request, 'gestionnote/update.html', {'form': lform, 'id': id})
        
    return HttpResponse("ok") 


def updateetudiant(request, id):
    etudiant = get_object_or_404(models.etudiants, pk=id)
    form = etudiantsForm(instance=etudiant)
    """
    if request.method == 'POST':
        form = LivreForm(instance=livre)
        if form.is_valid():
            form.save()
            return redirect('nom-de-la-page')
    """
    return render(request, 'gestionnote/updateetudiant.html', {'form': form, 'id': id})

def deleteetudiant(request, id):
    etudiant = get_object_or_404(models.etudiants, pk=id)
    etudiant.delete()
    return HttpResponseRedirect("/gestionnote/all/")










def ajoutrunite(request):
    if request.method == "POST":
        
        form = RuniteForm(request)
        if form.is_valid():
            runite = form.save()
            return render(request, 'gestionnote/afficherunite.html', {'runite': runite})
        else:
            return render(request, 'gestionnote/ajoutrunite.html', {'form': form})
    else:
        form = RuniteForm()
        return render(request, 'gestionnote/ajoutrunite.html', {'form': form})


def traitementrunite(request):
    lform = RuniteForm(request.POST)
    if lform.is_valid():
        runite = lform.save()
        return render(request, 'gestionnote/afficherunite.html', {'runite': runite})
    else:
        return render(request, 'gestionnote/ajoutrunite.html', {'form': lform})
    
    
def allrunite(request):
    runites = list(models.Runite.objects.all())
    return render(request, 'gestionnote/all.html', {'runites': runites})


def readrunite(request,id):
    runite = models.Runite.objects.get(pk=id)
    return render(request, 'gestionnote/afficherunite.html', {'runite': runite})

def traitementupdaterunite(request, id):
    lform = RuniteForm(request.POST)
    if lform.is_valid():
        
        runite = lform.save(commit=False)
        runite.id = id
        runite.save()
        return HttpResponseRedirect("/gestionnote/all/")
    else:
        return render(request, 'gestionnote/updaterunite.html', {'form': lform, 'id': id})
        
    return HttpResponse("ok") 


def updaterunite(request, id):
    runite = get_object_or_404(models.Runite, pk=id)
    form = RuniteForm(instance=runite)
    """
    if request.method == 'POST':
        form = LivreForm(instance=livre)
        if form.is_valid():
            form.save()
            return redirect('nom-de-la-page')
    """
    return render(request, 'gestionnote/updaterunite.html', {'form': form, 'id': id})

def deleterunite(request, id):
    runite = get_object_or_404(models.Runite, pk=id)
    runite.delete()
    return HttpResponseRedirect("/gestionnote/all/")








def ajoutunite(request):
    if request.method == "POST":
        
        form = UniteForm(request)
        if form.is_valid():
            unite = form.save()
            return render(request, 'gestionnote/afficheunite.html', {'unite': unite})
        else:
            return render(request, 'gestionnote/ajoutunite.html', {'form': form})
    else:
        form = UniteForm()
        return render(request, 'gestionnote/ajoutunite.html', {'form': form})


def traitementunite(request):
    lform = UniteForm(request.POST)
    if lform.is_valid():
        unite = lform.save()
        return render(request, 'gestionnote/afficheunite.html', {'unite': unite})
    else:
        return render(request, 'gestionnote/ajoutunite.html', {'form': lform})
    
    
def allunite(request):
    unites = list(models.Unite.objects.all())
    return render(request, 'gestionnote/all.html', {'unites': unites})


def readunite(request,id):
    unite = models.Unite.objects.get(pk=id)
    return render(request, 'gestionnote/afficheunite.html', {'unite': unite})

def traitementupdateunite(request, id):
    lform = UniteForm(request.POST)
    if lform.is_valid():
        
        unite = lform.save(commit=False)
        unite.id = id
        unite.save()
        return HttpResponseRedirect("/gestionnote/all/")
    else:
        return render(request, 'gestionnote/updateunite.html', {'form': lform, 'id': id})
        
    return HttpResponse("ok") 


def updateunite(request, id):
    unite = get_object_or_404(models.Unite, pk=id)
    form = UniteForm(instance=unite)
    """
    if request.method == 'POST':
        form = LivreForm(instance=livre)
        if form.is_valid():
            form.save()
            return redirect('nom-de-la-page')
    """
    return render(request, 'gestionnote/updateunite.html', {'form': form, 'id': id})

def deleteunite(request, id):
    unite = get_object_or_404(models.Unite, pk=id)
    unite.delete()
    return HttpResponseRedirect("/gestionnote/all/")






def ajoutnote(request):
    if request.method == "POST":
        
        form = NoteForm(request)
        if form.is_valid():
            note = form.save()
            return render(request, 'gestionnote/affichenote.html', {'note': note})
        else:
            return render(request, 'gestionnote/ajoutnote.html', {'form': form})
    else:
        form = NoteForm()
        return render(request, 'gestionnote/ajoutnote.html', {'form': form})


def traitementnote(request):
    lform = NoteForm(request.POST)
    if lform.is_valid():
        note = lform.save()
        return render(request, 'gestionnote/affichenote.html', {'note': note})
    else:
        return render(request, 'gestionnote/ajoutnote.html', {'form': lform})
    
    
def allnote(request):
    notes = list(models.Note.objects.all())
    return render(request, 'gestionnote/all.html', {'notes': notes})


def readnote(request,id):
    note = models.Note.objects.get(pk=id)
    return render(request, 'gestionnote/affichenote.html', {'note': note})

def traitementupdatenote(request, id):
    lform = NoteForm(request.POST)
    if lform.is_valid():
        
        note = lform.save(commit=False)
        note.id = id
        note.save()
        return HttpResponseRedirect("/gestionnote/all/")
    else:
        return render(request, 'gestionnote/updatenote.html', {'form': lform, 'id': id})
        
    return HttpResponse("ok") 


def updatenote(request, id):
    note = get_object_or_404(models.Note, pk=id)
    form = NoteForm(instance=note)
    """
    if request.method == 'POST':
        form = LivreForm(instance=livre)
        if form.is_valid():
            form.save()
            return redirect('nom-de-la-page')
    """
    return render(request, 'gestionnote/updatenote.html', {'form': form, 'id': id})

def deletenote(request, id):
    etudiant = get_object_or_404(models.Note, pk=id)
    etudiant.delete()
    return HttpResponseRedirect("/gestionnote/all/")
