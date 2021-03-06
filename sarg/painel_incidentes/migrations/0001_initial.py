# Generated by Django 2.1 on 2018-08-23 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OcorrenciasAbertasNoMes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_ocorrencia', models.CharField(max_length=100, unique=True)),
                ('titulo', models.CharField(max_length=200)),
                ('grupo_suporte', models.CharField(max_length=100)),
                ('tipo_servico', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'vw_painel_ocorrencias_abertas_no_mes_logstash',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OcorrenciasEmAberto',
            fields=[
                ('numero_ocorrencia', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('titulo', models.CharField(max_length=200)),
                ('data_criacao', models.DateField()),
                ('grupo_suporte', models.CharField(max_length=100)),
                ('tipo_servico', models.CharField(max_length=100)),
                ('situacao', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'vw_painel_ocorrencias_em_aberto_logstash',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OcorrenciasEmAbertoGraph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servico', models.CharField(max_length=100)),
                ('aguardando', models.DecimalField(decimal_places=2, max_digits=10)),
                ('atendimento', models.DecimalField(decimal_places=2, max_digits=10)),
                ('encaminhado', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'vw_painel_ocorrencias_em_aberto_graph',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OcorrenciasEncerradasMesAtual',
            fields=[
                ('numero_ocorrencia', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('titulo', models.CharField(max_length=200)),
                ('grupo_suporte', models.CharField(max_length=100)),
                ('tipo_servico', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'vw_painel_ocorrencias_encerradas_no_mes_atual_logstash',
                'managed': False,
            },
        ),
    ]
