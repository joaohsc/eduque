from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Materia(models.Model):
    titulo = models.CharField("Título",max_length=20, unique=True)
    descricao = models.TextField("Descrição")
    imagem = models.ImageField(upload_to='media/materia/', verbose_name="imagem")

    def get_absolute_url(self):
        return reverse('listagem_curso', kwargs={'pk' : self.pk})

    class Meta:
        verbose_name = 'Matéria'
        verbose_name_plural = 'Matérias'

    def __str__(self):
        return self.titulo

class Curso(models.Model):
    titulo = models.CharField("Título",max_length=50)
    descricao = models.TextField("Descrição")
    imagem = models.ImageField(upload_to='materia/', verbose_name="imagem", blank=True)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('listagem_aula', kwargs={'pk' : self.pk})

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.titulo

class Aula(models.Model):
    titulo = models.CharField("Título",max_length=50)
    descricao = models.TextField("Descrição")
    link = models.CharField("Link da Aula",max_length=300)
    conteudo = models.TextField("Conteúdo complementar")
    imagem = models.ImageField(upload_to='materia/', verbose_name="imagem", blank=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('detalhe_aula', kwargs={'pk' : self.pk})


    class Meta:
        verbose_name = 'Aula'
        verbose_name_plural = 'Aulas'

    def __str__(self):
        return self.titulo

class Evento(models.Model):
    titulo = models.CharField("Título",max_length=50)
    data = models.DateField()
    descricao = models.TextField("Descrição")
    link = models.CharField("Site do evento",max_length=300)
    imagem = models.ImageField(upload_to='materia/', verbose_name="imagem", blank=True)
    inscritos = models.ManyToManyField(User, blank=True)
    num_inscritos = models.IntegerField(verbose_name="Número de Inscritos", default=0)

    def get_absolute_url(self):
        return reverse('detalhe_evento', kwargs={'pk' : self.pk})

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    def __str__(self):
        return self.titulo