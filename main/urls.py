from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

from .decorators import *

urlpatterns = [
    path('', views.index, name='index'),
    path('perfil/', views.perfil, name='perfil'),
    path('registro/', views.registro, name='registro'),
    path('login/', unauthenticated_user(auth_view.LoginView.as_view(template_name='login.html')), name='login'),
    path('logout/', authenticated_user(auth_view.LogoutView.as_view(template_name='login.html')), name='logout'),
    #views da matéria
    path('materias/', views.MateriaList, name='listagem_materia'),
    path('materias/cadastrar/', views.MateriaCreate.as_view(), name='cadastrar_materia'),
    path('materias/editar/<int:pk>/', views.MateriaUpdate.as_view(), name='atualizar_materia'),
    path('materias/deletar/<int:pk>/',views.MateriaDelete.as_view(), name='deletar_materia'),
    #views do curso
    path('materia/<int:materia_id>/', views.CursoList, name='listagem_curso'),
    path('materia/<int:materia_id>/cadastrar_curso/', views.CursoCreate.as_view(), name='cadastrar_curso'),
    path('materia/<int:materia_id>/editar_curso/<int:pk>/', views.CursoUpdate.as_view(), name='atualizar_curso'),
    path('materia/<int:materia_id>/deletar_curso/<int:pk>/',views.CursoDelete.as_view(), name='deletar_curso'),
    #views da aula
    path('materia/<int:materia_id>/<int:curso_id>/', views.AulaList, name='listagem_aula'),
    path('materia/<int:materia_id>/<int:curso_id>/<int:aula_id>/', views.AulaDetail, name='detalhe_aula'),
    path('materia/<int:materia_id>/<int:curso_id>/cadastrar_aula/', views.AulaCreate.as_view(), name='cadastrar_aula'),
    path('materia/<int:materia_id>/<int:curso_id>/<int:pk>/editar_aula/', views.AulaUpdate.as_view(), name='atualizar_aula'),
    path('materia/<int:materia_id>/<int:curso_id>/<int:pk>/deletar_aula/',views.AulaDelete.as_view(), name='deletar_aula'),
    #views do evento
    path('eventos/', views.EventoList, name='listagem_evento'),
    path('evento/<int:pk>', views.EventoDetail, name='detalhe_evento'),
    path('evento/cadastro/', views.EventoCreate.as_view(), name='cadastrar_evento'),
    path('evento/editar/<int:pk>/', views.EventoUpdate.as_view(), name='atualizar_evento'),
    path('evento/deletar/<int:pk>/',views.EventoDelete.as_view(), name='deletar_evento'),
]