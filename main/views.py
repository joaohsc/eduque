from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import Group
from .forms import *
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import *
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
            return render(request, 'professor/prof_home.html')
    else:
        return redirect('login')

@login_required(login_url='login')
def perfil(request):
    if request.user.groups.exists():
        group = request.user.groups.all()[0].name
        user = request.user
        form = UserUpdateForm(instance=user)

        if request.method == "POST":
            form = UserUpdateForm(data=request.POST, instance=request.user)
            if form.is_valid():
                update = form.save(commit=False)
                update.user = request.user
                update.save()
            
        
        context={
            'user' : user,
            'form' : form,
        }
        if group == 'aluno':
            return render(request, 'aluno/aluno_perfil.html', context)
        else:
            return render(request, 'professor/prof_perfil.html', context)
    else:
        return redirect('login')

@unauthenticated_user
def registro(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            tipo_usuario = form.cleaned_data.get('tipo_de_usuario')
            if tipo_usuario == 'ALUNO':
                group = Group.objects.get(name='aluno')
                user.groups.add(group)
            else:
                group = Group.objects.get(name='administrador')
                user.groups.add(group)
            
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
    if request.user.groups.exists():
        materias = Materia.objects.all()
        context={
            'materias' : materias,
        }
    
        group = request.user.groups.all()[0].name
        if group == 'aluno':
            return render(request, 'aluno/aluno_materia.html', context)
        else:
            return render(request, 'professor/prof_materia.html', context)
    else:
        return redirect('login')
    
@login_required(login_url='login')
@allowed_users(allowed_roles=['administrador', 'aluno'])
def CursoList(request, materia_id):
    if request.user.groups.exists():
        pk = materia_id
        materia = get_object_or_404(Materia, pk=pk) 
        cursos = Curso.objects.filter(materia=pk)
        group = request.user.groups.all()[0].name
        context={
            'cursos' : cursos,
            'materia' : materia,
        }
        if group == 'aluno':
            return render(request, 'aluno/aluno_cursos.html', context)
        else:
            return render(request, 'professor/prof_cursos.html', context)
        return render(request, 'materia.html', context)
    else:
        return redirect('login')

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
def AulaList(request, materia_id, curso_id):
    if request.user.groups.exists():
        
        materia = get_object_or_404(Materia, id=materia_id) 
        curso = get_object_or_404(Curso, id=curso_id) 
        aulas = Aula.objects.filter(curso=curso_id)

        context={
            'materia' : materia,
            'curso' : curso,
            'aulas' : aulas,
        }
    
        group = request.user.groups.all()[0].name
        if group == 'aluno':
            return render(request, 'aluno/aluno_aulas.html', context)
        else:
            return render(request, 'professor/prof_aulas.html', context)
    else:
        return redirect('login')

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
@login_required(login_url='login')
@allowed_users(allowed_roles=['administrador', 'aluno'])
def AulaDetail(request, materia_id, curso_id, aula_id):
    if request.user.groups.exists():

        materia = get_object_or_404(Materia, id=materia_id) 
        curso = get_object_or_404(Curso, id=curso_id) 
        aula = get_object_or_404(Aula,id=aula_id)

        context={
            'materia' : materia,
            'curso' : curso,
            'aula' : aula,
        }
    
        group = request.user.groups.all()[0].name
        if group == 'aluno':
            return render(request, 'aluno/aluno_aula.html', context)
        else:
            return render(request, 'professor/prof_aula.html', context)
    else:
        return redirect('login')

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
@login_required(login_url='login')
@allowed_users(allowed_roles=['administrador', 'aluno'])
def EventoDetail(request, pk):
    if request.user.groups.exists():
        evento = get_object_or_404(Evento, id=pk) 
        context={
            'evento' : evento,
        }
        group = request.user.groups.all()[0].name
        if group == 'aluno':
            return render(request, 'aluno/aluno_inscricao.html', context)
        else:
            return render(request, 'professor/prof_inscricao.html', context)
    else:
        return redirect('login')

@login_required(login_url='login')
@allowed_users(allowed_roles=['administrador', 'aluno'])
def InscricaoList(request):
    #EXEMPLO APENAS PARA PREENCHER A PÁGINA DE LISTA DE INSCRIÇÕES

    if request.user.groups.exists():
        eventos = Evento.objects.all() 
        context={
            'eventos' : eventos,
        }
        group = request.user.groups.all()[0].name
        if group == 'aluno':
            return render(request, 'aluno/aluno_inscricoes.html', context)
        else:
            return render(request, 'professor/prof_inscricoes.html', context)
    else:
        return redirect('login')

@login_required(login_url='login')
@allowed_users(allowed_roles=['administrador', 'aluno'])
def EventoList(request): 
    if request.user.groups.exists():
        eventos = Evento.objects.all()
        context={
            'eventos' : eventos,
        }
    
        group = request.user.groups.all()[0].name
        if group == 'aluno':
            return render(request, 'aluno/aluno_eventos.html', context)
        else:
            return render(request, 'professor/prof_eventos.html', context)
    else:
        return redirect('login')
    
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
