from .base_model import BaseModel
from enums import Tipo_Projeto

from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from django.utils import timezone
from django.core.exceptions import ValidationError

class Projeto(BaseModel):
    codigo = models.CharField(validators=[MinLengthValidator(5)], 
                              max_length=20, 
                              unique=True,
                              verbose_name='Código do Projeto:',
                              help_text='Digite um código único para o projeto (mínimo 5 caracteres).')
    
    nome = models.CharField(validators=[MinLengthValidator(5)],
                           max_length=100,
                           blank=False,
                           null=False,
                           verbose_name='Nome do Projeto:',
                            help_text='Digite o nome do projeto (mínimo 5 caracteres).')
    
    tipo_projeto = models.CharField(choices=Tipo_Projeto.choices,
                                    blank=False,
                                    null=False,
                                    verbose_name='Tipo de Projeto:',
                                    help_text='Selecione o tipo do projeto.')

    cliente = models.CharField(validators=[MinLengthValidator(3)],
                               max_length=50,
                               blank=False,
                               null=False,
                               verbose_name='Cliente:',
                               help_text='Digite o nome do cliente (mínimo 3 caracteres).')
    
    gerente = models.CharField(validators=[MinLengthValidator(3)],
                              max_length=50,
                              blank=False,
                              null=False,
                              verbose_name='Gerente do Projeto:',
                              help_text='Digite o nome do gerente do projeto (mínimo 3 caracteres).')
    
    inicio = models.DateField(validators=[MinValueValidator(timezone.now().date())],
                              verbose_name='Data de Início:',
                              help_text='Selecione a data de início do projeto.')
    
    previsao_de_termino = models.DateField(validators=[MinValueValidator(inicio)],
                                            blank=False,
                                            null=False,
                                            verbose_name='Previsão de Término:',
                                            help_text='Selecione a data de previsão de término do projeto (deve ser após a data de início).')
    
    fim = models.DateField(MinValueValidator(inicio),
                           blank=True,
                           null=True,
                           verbose_name='Data de Término:',
                           help_text='Selecione a data de término do projeto (deve ser após a data de início).')
    
    orcamento = models.DecimalField(validators=[MinValueValidator(2)],
                                    verbose_name='Orçamento:',
                                    help_text='Digite o orçamento do projeto (valor mínimo 2).')
    
    ativo = models.BooleanField(default=True, 
                                verbose_name='Ativo:', 
                                help_text='Indica se o projeto está ativo.')
    
    def __str__(self):
        return f"{self.codigo} - {self.nome}"
    
    def clean(self):
        if self.inicio and self.previsao_de_termino:
             if self.previsao_termino < self.inicio:
                raise ValidationError({
                    "previsao_termino": "A previsão de término não pode ser anterior à data de início",
                })
        if self.inicio and self.fim:
            if self.fim < self.inicio:
                raise ValidationError({
                    "fim": "O fim não pode ser anterior á data de início",
                })