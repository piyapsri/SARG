from django.db import models
# Create your models here.
class Clientes(models.Model):
    id = models.AutoField(primary_key=True)
    logo = models.ImageField(upload_to='media',  blank=True, null=False)
    cliente = models.CharField(u'Cliente', max_length = 150, blank=True, null=False)
    def __str__(self):
        return '%s' % (self.cliente)

    class Meta:
        verbose_name = "Clientes"
        verbose_name_plural = "Clientes"

