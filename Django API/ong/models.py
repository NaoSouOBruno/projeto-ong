from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    animal = models.CharField(max_length=30)
    sexo = models.CharField(max_length=10)
    raca = models.CharField(max_length=30)
    idade = models.CharField(max_length=10)

    def __str__(self):
        return self.nome
