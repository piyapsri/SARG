# Generated by Django 2.1 on 2018-08-22 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('painel_demandas', '0002_auto_20180822_0930'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='demandas',
            table='vw_painel_demandas_logstash',
        ),
    ]
