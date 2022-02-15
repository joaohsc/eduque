from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

from .decorators import *

urlpatterns = [
    path('', views.index, name='index'),
    path('registro/', views.registro, name='registro'),
    path('login/', unauthenticated_user(auth_view.LoginView.as_view(template_name='login.html')), name='login'),
    path('logout/', authenticated_user(auth_view.LogoutView.as_view(template_name='login.html')), name='logout'),
    #views da matéria
    path('materias/', views.MateriaList, name='listagem_materia'),
    path('materia/cadastro/', views.MateriaCreate.as_view(), name='cadastrar_materia'),
    path('materia/atualização/<int:pk>/', views.MateriaUpdate.as_view(), name='atualizar_materia'),
    path('materia/<int:pk>/deletar/',views.MateriaDelete.as_view(), name='deletar_materia'),
    #views do curso
    path('materia/<int:pk>/', views.CursoList, name='listagem_curso'),
    path('materia/curso/cadastro/', views.CursoCreate.as_view(), name='cadastrar_curso'),
    path('materia/curso/atualização/<int:pk>/', views.CursoUpdate.as_view(), name='atualizar_curso'),
    path('materia/curso/<int:pk>/deletar/',views.CursoDelete.as_view(), name='deletar_curso'),
    #views da aula
    path('materia/curso/<int:pk>', views.AulaList, name='listagem_aula'),
    path('materia/curso/aula/<int:pk>', views.AulaDetail.as_view(), name='detalhe_aula'),
    path('materia/curso/aula/cadastro', views.AulaCreate.as_view(), name='cadastrar_aula'),
    path('materia/curso/aula/atualização/<int:pk>/', views.AulaUpdate.as_view(), name='atualizar_aula'),
    path('materia/curso/aula/<int:pk>/deletar/',views.AulaDelete.as_view(), name='deletar_aula'),
    #views do evento
    path('eventos/', views.EventoList.as_view(), name='listagem_evento'),
    path('evento/<int:pk>', views.EventoDetail.as_view(), name='detalhe_evento'),
    path('evento/cadastro/', views.EventoCreate.as_view(), name='cadastrar_evento'),
    path('evento/atualização/<int:pk>/', views.EventoUpdate.as_view(), name='atualizar_evento'),
    path('evento/<int:pk>/deletar/',views.EventoDelete.as_view(), name='deletar_evento'),
]