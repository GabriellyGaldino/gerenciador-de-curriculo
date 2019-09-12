from django.db import models
from django.contrib.auth.models import AbstractUser, Permission
import uuid

# Create your models here.

class User(AbstractUser):
    SEXO = (
        (1,'Masculino'),
        (2,'Feminino'),
        (3,'Indefinido')
    )

    user_permissions = models.ManyToManyField(Permission, blank=True, related_name="uuiduser_set", related_query_name="user")

    date_of_birth = models.DateTimeField('Data de Nascimento', auto_now=True)
    address = models.CharField(max_length=100, verbose_name='Endereço')
    genre = models.IntegerField(choices=SEXO, verbose_name = 'Gênero', default=3)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

class Category(models.Model):
    category = models.CharField(max_length=100,  verbose_name='Categoria')

    def __str__(self):
        return self.category
        
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Productions(models.Model):
    production = models.CharField(max_length=100,  verbose_name='production')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='production')
    # arquivo = models.FileField

    def __str__(self):
        return self.production

    class Meta:
        verbose_name = 'Producao'
        verbose_name_plural = 'Producoes'

class Curriculum(models.Model):
    objetivo = models.CharField(max_length=100)
    formacao= models.CharField(max_length=100)
    experiencia = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Proprietario")
    production = models.ForeignKey(Productions, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Curriculo'
        verbose_name_plural = 'Curriculos'