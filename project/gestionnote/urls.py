from django.urls import path
from . import views


urlpatterns = [
  path('login/', views.login_view, name='login'),
  path('', views.main, name='main'),
  path('ajout/', views.ajout, name='ajout'),  
  path('traitement/', views.traitement , name='traitement'),
  path('all/', views.all, name='all'),
  path('read/<int:id>', views.read, name='read'),
  path('update/<int:id>', views.update, name='update',),
  path('traitementupdate/<int:id>', views.traitementupdate, name='traitementupdate'),
  path('delete/<int:id>', views.delete, name='delete'),



  path('ajoutenseignant/', views.ajoutenseignant, name='ajoutenseignant'),  
  path('traitementenseignant/', views.traitementenseignant , name='traitementenseignant'),
  path('allenseignant/', views.allenseignant, name='allenseignant'),
  path('readenseignant/<int:id>', views.readenseignant, name='readenseignant'),
  path('updateenseignant/<int:id>', views.updateenseignant, name='updateenseignant',),
  path('traitementupdateenseignant/<int:id>', views.traitementupdateenseignant, name='traitementupdateenseignant'),
  path('deleteenseignant/<int:id>', views.deleteenseignant, name='deleteenseignant'),
  



  path('ajoutetudiant/', views.ajoutetudiant, name='ajoutetudiant'),  
  path('traitementetudiant/', views.traitementetudiant , name='traitraitementetudianttement'),
  path('alletudiant/', views.alletudiant, name='alletudiant'),
  path('readetudiant/<int:id>', views.readetudiant, name='readetudiant'),
  path('updateetudiant/<int:id>', views.updateetudiant, name='updateetudiant',),
  path('traitementupdateetudiant/<int:id>', views.traitementupdateetudiant, name='traitementupdateetudiant'),
  path('deleteetudiant/<int:id>', views.deleteetudiant, name='deleteetudiant'),
 



  path('ajoutrunite', views.ajoutrunite, name='ajout'),  
  path('traitementrunite/', views.traitementrunite , name='traitement'),
  path('allrunite/', views.allrunite, name='all'),
  path('readrunite/<int:id>', views.readrunite, name='read'),
  path('updaterunite/<int:id>', views.updaterunite, name='update',),
  path('traitementupdaterunite/<int:id>', views.traitementupdaterunite , name='traitementupdate'),
  path('deleterunite/<int:id>', views.deleterunite, name='delete'),
  




  path('ajoutunite/', views.ajoutunite, name='ajout'),  
  path('traitementunite/', views.traitementunite , name='traitement'),
  path('allunite/', views.allunite, name='all'),
  path('readunite/<int:id>', views.readunite, name='read'),
  path('updateunite/<int:id>', views.updateunite, name='update',),
  path('traitementupdateunite/<int:id>', views.traitementupdateunite, name='traitementupdate'),
  path('deleteunite/<int:id>', views.deleteunite, name='delete'),
  



  path('ajoutnote', views.ajoutnote, name='ajout'),  
  path('traitementnote/', views.traitementnote , name='traitement'),
  path('allnote/', views.all, name='all'),
  path('readnote/<int:id>', views.readnote, name='read'),
  path('updatenote/<int:id>', views.updatenote, name='update',),
  path('traitementupdatenote/<int:id>', views.traitementupdatenote, name='traitementupdate'),
  path('deletenote/<int:id>', views.deletenote, name='delete'),
]