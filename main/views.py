from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import *

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

def index(request):
    return render(request, 'index.html')

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

def MateriaList(request):
    materias = Materia.objects.all()
    context={
        'materias' : materias,
    }
    return render(request, 'materias.html', context)

def CursoList(request, pk):
    pk = pk
    materia = get_object_or_404(Materia, pk=pk) 
    cursos = Curso.objects.filter(materia=pk)
    context={
        'cursos' : cursos,
        'materia' : materia,
    }
    return render(request, 'materia.html', context)

def AulaList(request, pk):
    pk = pk
    curso = get_object_or_404(Curso, pk=pk) 
    aulas = Aula.objects.filter(curso=pk)
    context={
        'curso' : curso,
        'aulas' : aulas,
    }
    return render(request, 'aulas.html', context)

#views da classe Aula
@method_decorator(login_required, name='dispatch')
class AulaDetail(generic.DetailView):
    model = Aula
    template_name = 'aula.html'
    queryset_name = 'aula'

@method_decorator(login_required, name='dispatch')
class AulaCreate(CreateView):
    model = Aula
    fields = ['titulo', 'descricao', 'link', 'conteudo', 'imagem', 'curso']
    template_name = 'aula_form.html'

@method_decorator(login_required, name='dispatch')
class AulaUpdate(UpdateView):
    model = Aula
    fields = ['titulo', 'descricao', 'link', 'conteudo', 'imagem', 'curso']
    template_name = 'aula_form.html'

@method_decorator(login_required, name='dispatch')  
class AulaDelete(DeleteView):
    model = Aula
    template_name = 'aula_form.html'
    success_url = reverse_lazy('listagem_materia')

@method_decorator(login_required, name='dispatch')
class EventoDetail(generic.DetailView):
    model = Evento
    template_name = 'evento.html'
    queryset_name = 'evento'

@method_decorator(login_required, name='dispatch')
class EventoList(generic.ListView):
    template_name = 'eventos.html'
    context_object_name = 'eventos'

    def get_queryset(self):
        return Evento.objects.all

