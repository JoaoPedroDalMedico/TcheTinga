from django.db.models import TextChoices


class Linguagem_Programacao(TextChoices):
    PYTHON = 'Python', 'Python'
    JAVA = 'Java', 'Java'
    JS = 'JavaScript', 'JavaScript'
    CSHARP = 'C#', 'C#'
    CPLUSPLUS = 'C++', 'C++'
    C = 'C', 'C'
    DART = 'Dart', 'Dart'
    PHP = 'PHP', 'PHP'