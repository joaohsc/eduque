# Generated by Django 4.0.2 on 2022-02-14 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_materia_slug_alter_materia_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='imagem',
            field=models.ImageField(null=True, upload_to='materia/', verbose_name='imagem'),
        ),
    ]
