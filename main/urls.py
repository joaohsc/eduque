from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.index, name='index'),
    path('registro/', views.registro, name='registro'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    #views da matéria
    path('materias/', views.MateriaList, name='listagem_materia'),
    #views do curso
    path('materia/<int:pk>/', views.CursoList, name='listagem_curso'),
    #views da aula
    path('materia/curso/<int:pk>', views.AulaList, name='listagem_aula'),
    path('materia/curso/aula/<int:pk>', views.AulaDetail.as_view(), name='detalhe_aula'),
    path('materia/curso/aula/cadastro', views.AulaCreate.as_view(), name='cadastrar_aula'),
    path('materia/curso/aula/atualização/<int:pk>/', views.AulaUpdate.as_view(), name='atualizar_aula'),
    path('author/<int:pk>/delete/',views.AulaDelete.as_view(), name='deletar_aula'),
    #views do evento
    path('eventos/', views.EventoList.as_view(), name='listagem_evento'),
    path('evento/<int:pk>', views.EventoDetail.as_view(), name='detalhe_evento'),
]