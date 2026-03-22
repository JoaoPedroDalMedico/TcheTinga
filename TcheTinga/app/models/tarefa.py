from .base_model import BaseModel
from enums import Satus, Linguagem_Programacao

from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from django.core.exceptions import ValidationError


class Tarefa(BaseModel):
    titulo = models.CharField(validators=[MinLengthValidator(5)],
                              max_length=100,
                              blank=False,
                              null=False,
                              verbose_name='Título da Tarefa:',
                              help_text='Digite o título da tarefa (mínimo 5 caracteres).')
    
    descricao = models.TextField(blank=True, 
                                 null=True,
                                 validators=[MinLengthValidator(0)],
                                 max_length=1000,
                                 verbose_name='Descrição da Tarefa:',
                                 help_text='Digite uma descrição para a tarefa (opcional).')
    
    linguagem_programacao = models.CharField(choices=Linguagem_Programacao.choices,
                                             blank=False,
                                             null=False,
                                             verbose_name='Linguagem de Programação:',
                                             help_text='Selecione a linguagem de programação associada à tarefa.')

    estimativa_horas = models.IntegerField(validators=[MinValueValidator(0),],
                                           help_text='Insira a estimativa de horas da tarefa',
                                           verbose_name='Estimativa de horas:',)
    
    horas_registradas = models.PositiveIntegerField(validators=[MinValueValidator(0)],
                                            default=0,
                                            help_text='Insira as horas resgitradas da tarefa',
                                            verbose_name='Horas resgitradas:',)

    prioridade = models.PositiveIntegerField(min_value=1,
                                             max_value=5,
                                             verbose_name='Prioridade da Tarefa:',
                                             help_text='Defina a prioridade da tarefa (1-5).')
    
    satus = models.CharField(choices=Satus.choices,
                             blank=False,
                            null=False,
                            verbose_name='Status da Tarefa:',
                            help_text='Selecione o status da tarefa.')

    responsavel = models.CharField(validators=[MinLengthValidator(3)],
                                   max_length=50,
                                   blank=False,
                                   null=False,)
    
    criacao = models.DateTimeField(blank=False,
                                   null=False,
                                   verbose_name='Data de Criação:',
                                   help_text='Data e hora em que a tarefa foi criada.')
    
    conlusao = models.DateTimeField(blank=True,
                                    null=True,
                                    validators=[MinValueValidator(criacao)],
                                    verbose_name='Data de Conclusão:',
                                    help_text='Data e hora em que a tarefa foi concluída (opcional).')
    
    def __str__(self):
        return f"{self.titulo} -  {self.responsavel}"
    
    def clean(self):
        super().clean()

        # Projeto obrigatório
        if not self.projeto:
            raise ValidationError({
                'projeto': 'A tarefa deve estar associada a um projeto.'
            })

        # Projeto fechado (inativo ou com data fim)
        if not self.projeto.ativo or self.projeto.fim:
            raise ValidationError({
                'projeto': 'Não é possível criar tarefas em um projeto encerrado.'
            })

        # Data de criação anterior ao início do projeto
        if self.criacao and self.projeto.inicio:
            if self.criacao < self.projeto.inicio:
                raise ValidationError({
                    'criacao': 'A data de criação da tarefa não pode ser anterior ao início do projeto.'
                })
    