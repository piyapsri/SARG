# Generated by Django 2.1 on 2018-09-14 13:08

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
        ('cadastro_financeiro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HORAS_ONGOING',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('item_contabil', models.CharField(max_length=255)),
                ('hora_total', models.CharField(max_length=255)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PROJETOS',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('projeto', models.CharField(blank=True, max_length=150, verbose_name='Projeto')),
                ('gp', models.CharField(blank=True, max_length=75, verbose_name='GP')),
                ('responsavel_tecnico', models.CharField(blank=True, max_length=75, verbose_name='Responsável Técnico')),
                ('data_inicio', models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='Data Inicio')),
                ('data_fim', models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='Data Fim')),
                ('horas_previstas', models.IntegerField(blank=True, null=True, verbose_name='Horas Previstas')),
                ('percent_conclusao', models.CharField(blank=True, max_length=4, verbose_name='Percentual Conclusão')),
                ('fase', models.CharField(blank=True, max_length=75, verbose_name='Fase')),
                ('status', models.CharField(blank=True, choices=[('1', 'OK'), ('2', 'Atenção'), ('3', 'Problema'), ('4', 'Pausado'), ('5', 'Inativo')], max_length=30, null=True)),
                ('categoria', models.CharField(blank=True, choices=[('1', 'OnGoing'), ('2', 'Projeto')], max_length=30, null=True)),
                ('obs', models.TextField(blank=True, null=True, verbose_name='Observação')),
                ('historico', models.TextField(blank=True, verbose_name='Histórico')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.Clientes', verbose_name='Cliente')),
                ('codigo_atividade', models.ManyToManyField(to='cadastro_financeiro.Atividade', verbose_name='Cód. Atividade')),
                ('item_contabil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro_financeiro.ItemContabil', verbose_name='Item Contábil')),
            ],
            options={
                'verbose_name': 'Painel de Projetos',
                'verbose_name_plural': 'Projetos',
            },
        ),
    ]
