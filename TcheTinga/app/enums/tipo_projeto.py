from django.db.models import TextChoices

class Tipo_Projeto(TextChoices):
    WEB = 'Desenvolvimento Web', 'Desenvolvimento Web'
    MOBILE = 'Aplicativo de celular', 'Aplicativo de celular'
    DESKTOP = 'Aplicação Desktop', 'Aplicação Desktop'
    API = 'Web Services/API', 'Web Services/API'
    LIBRARY = 'LIBRARY', 'Projeto de Ciência de Dados'
    AI = 'Inteligência Artificial', 'Inteligência Artificial'