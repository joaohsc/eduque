from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django import forms

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    TIPO_DE_USUARIO = [
        ('ALUNO', 'Aluno'),
        ('EMPRESA', 'Empresa'),
        ('PROFESSOR', 'Professor'),
    ]
    tipo_de_usuario = forms.ChoiceField(choices = TIPO_DE_USUARIO)

    class Meta: 
        model = User
        fields = ['username', 'email', 'tipo_de_usuario', 'password1', 'password2']