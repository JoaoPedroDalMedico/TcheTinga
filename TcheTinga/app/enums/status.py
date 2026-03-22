from django.db.models import TextChoices


class Satus(TextChoices):
    PENDENTE = 'Pendente', 'Pendente'
    EM_ANDAMENTO = 'Em Andamento', 'Em Andamento'
    CONCLUIDA = 'Concluída', 'Concluída'
    ATRASADA = 'Atrasada', 'Atrasada'