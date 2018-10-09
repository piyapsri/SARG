from django.db import models

# Create your models here.
from django.contrib.auth.models import User

# Create your models here.
class homeImagens(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(u'Titulo', max_length = 150, blank=False, null=False)
    sub_titulo = models.CharField(u'Sub Titulo', max_length = 150, blank=False, null=False)
    imagem = models.ImageField(upload_to='media',  blank=False, null=False)
    status_choices = (
    ('','Selecione'),
    ('Ativo', 'Ativo'),
    ('Inativo', 'Inativo')
    )
    status = models.CharField(u'Status', max_length = 10, choices=status_choices, blank=False, null=False, default='')
    def __str__(self):
        return '%s' % (self.titulo)

    class Meta:
        verbose_name = "Imagens"
        verbose_name_plural = "Imagens"