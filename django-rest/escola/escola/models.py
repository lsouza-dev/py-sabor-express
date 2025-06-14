from django.db import models

class Estudante(models.Model):
    nome = models.CharField(max_length=100,null=False,blank=False)
    email = models.EmailField(max_length=30,blank=False)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    celular = models.CharField(max_length=14)


    def __str__(self):
        return self.nome


class Curso(models.Model):
    NIVEL = (
        ('B','Básico'),
        ('I','Intermediário'),
        ('A','Avançado'),
    )
    codigo = models.CharField(max_length=10)
    descricao = models.CharField(blank=False,max_length=100)
    nivel = models.CharField(max_length=1, choices = NIVEL, blank=False, null=False , default= 'B')

    def __str__(self):
        return self.codigo
    