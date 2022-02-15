from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import *
from django.contrib.auth import views as auth_view
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .decorators import *

@login_required(login_url='login')
def index(request):
    if request.user.groups.exists():
        group = request.user.groups.all()[0].name
        if group == 'aluno':
            return render(request, 'aluno/aluno_home.html')
        else:
            return render(request, 'index2.html')
    else:
        return redirect('login')

@unauthenticated_user
def registro(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            usuario = form.cleaned_data.get('usuario')
            messages.success(request, f'{usuario}, sua conta foi criada com sucesso!') 
            return redirect('index')
    else:
        form = UserRegisterForm()

    context = {
        'form' : form,
    }

    return render(request, 'registro.html', context)

#views da classe Materia
@login_required(login_url='login')
@allowed_users(allowed_roles=['administrador', 'aluno'])
def MateriaList(request):
    materias = Materia.objects.all()
    context={
        'materias' : materias,
    }
    return render(request, 'materias.html', context)
@login_required(login_url='login')
@allowed_users(allowed_roles=['administrador', 'aluno'])
def CursoList(request, pk):
    pk = pk
    materia = get_object_or_404(Materia, pk=pk) 
    cursos = Curso.objects.filter(materia=pk)
    context={
        'cursos' : cursos,
        'materia' : materia,
    }
    return render(request, 'materia.html', context)

@method_decorator(login_required(login_url='login'), name='dispatch')
@method_decorator(allowed_users(allowed_roles=['administrador']), name='dispatch') 
class MateriaCreate(CreateView):
    model = Materia
    fields = ['titulo', 'descricao', 'imagem']
    template_name = 'aula_form.html'

@method_decorator(login_required(login_url='login'), name='dispatch')
@method_decorator(allowed_users(allowed_roles=['administrador']), name='dispatch') 
class MateriaUpdate(UpdateView):
    model = Materia
    fields = ['titulo', 'descricao', 'imagem']
    template_name = 'aula_form.html'

@method_decorator(login_required(login_url='login'), name='dispatch')
@method_decorator(allowed_users(allowed_roles=['administrador']), name='dispatch')   
class MateriaDelete(DeleteView):
    model = Materia
    template_name = 'aula_form.html'
    success_url = reverse_lazy('listagem_materia')

#views da classe Curso
@login_required(login_url='login')
@allowed_users(allowed_roles=['administrador', 'aluno'])
def AulaList(request, pk):
    pk = pk
    curso = get_object_or_404(Curso, pk=pk) 
    aulas = Aula.objects.filter(curso=pk)
    context={
        'curso' : curso,
        'aulas' : aulas,
    }
    return render(request, 'aulas.html', context)

@method_decorator(login_required(login_url='login'), name='dispatch')
@method_decorator(allowed_users(allowed_roles=['administrador']), name='dispatch') 
class CursoCreate(CreateView):
    model = Curso
    fields = ['titulo', 'descricao', 'imagem', 'materia']
    template_name = 'aula_form.html'

@method_decorator(login_required(login_url='login'), name='dispatch')
@method_decorator(allowed_users(allowed_roles=['administrador']), name='dispatch') 
class CursoUpdate(UpdateView):
    model = Curso
    fields = ['titulo', 'descricao', 'imagem', 'materia']
    template_name = 'aula_form.html'

@method_decorator(login_required(login_url='login'), name='dispatch')
@method_decorator(allowed_users(allowed_roles=['administrador']), name='dispatch')  
class CursoDelete(DeleteView):
    model = Curso
    template_name = 'aula_form.html'
    success_url = reverse_lazy('listagem_materia')

#views da classe Aula
@method_decorator(login_required(login_url='login'), name='dispatch')
@method_decorator(allowed_users(allowed_roles=['administrador', 'aluno']), name='dispatch') 
class AulaDetail(generic.DetailView):
    model = Aula
    template_name = 'aula.html'
    queryset_name = 'aula'

@method_decorator(login_required(login_url='login'), name='dispatch')
@method_decorator(allowed_users(allowed_roles=['administrador']), name='dispatch') 
class AulaCreate(CreateView):
    model = Aula
    fields = ['titulo', 'descricao', 'link', 'conteudo', 'imagem', 'curso']
    template_name = 'aula_form.html'

@method_decorator(login_required(login_url='login'), name='dispatch')
@method_decorator(allowed_users(allowed_roles=['administrador']), name='dispatch') 
class AulaUpdate(UpdateView):
    model = Aula
    fields = ['titulo', 'descricao', 'link', 'conteudo', 'imagem', 'curso']
    template_name = 'aula_form.html'

@method_decorator(login_required(login_url='login'), name='dispatch')
@method_decorator(allowed_users(allowed_roles=['administrador']), name='dispatch') 
class AulaDelete(DeleteView):
    model = Aula
    template_name = 'aula_form.html'
    success_url = reverse_lazy('listagem_materia')

#views da classe Evento
@method_decorator(login_required(login_url='login'), name='dispatch')
@method_decorator(allowed_users(allowed_roles=['administrador', 'aluno']), name='dispatch') 
class EventoDetail(generic.DetailView):
    model = Evento
    template_name = 'evento.html'
    queryset_name = 'evento'

@method_decorator(login_required(login_url='login'), name='dispatch')
@method_decorator(allowed_users(allowed_roles=['administrador', 'aluno']), name='dispatch') 
class EventoList(generic.ListView):
    template_name = 'eventos.html'
    context_object_name = 'eventos'

    def get_queryset(self):
        return Evento.objects.all

@method_decorator(login_required(login_url='login'), name='dispatch')
@method_decorator(allowed_users(allowed_roles=['administrador']), name='dispatch') 
class EventoCreate(CreateView):
    model = Evento
    fields = ['titulo','data', 'descricao', 'link', 'imagem']
    template_name = 'aula_form.html'

@method_decorator(login_required(login_url='login'), name='dispatch')
@method_decorator(allowed_users(allowed_roles=['administrador']), name='dispatch') 
class EventoUpdate(UpdateView):
    model = Evento
    fields = ['titulo','data', 'descricao', 'link', 'imagem']
    template_name = 'aula_form.html'

@method_decorator(login_required(login_url='login'), name='dispatch')
@method_decorator(allowed_users(allowed_roles=['administrador']), name='dispatch') 
class EventoDelete(DeleteView):
    model = Evento
    template_name = 'aula_form.html'
    success_url = reverse_lazy('listagem_evento')
