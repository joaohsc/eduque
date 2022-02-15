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

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput(), label='Senha')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Confirmação de Senha')
    class Meta: 
        model = User
        fields = ['username', 'email', 'password1', 'password2']