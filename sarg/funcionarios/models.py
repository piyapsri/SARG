from django.db import models

# Create your models here.

class Contrato(models.Model):
	id = models.AutoField(primary_key=True)
	contrato = models.CharField(u'Contrato', max_length=155, blank=False, null=False, unique=True)
	def __str__(self):
		return '%s' % (self.contrato)
	class meta:
		verbose_name = 'Contrato'
		verbose_name_plural = 'Contratos'
		
class Departamento(models.Model):
	id = models.AutoField(primary_key=True)
	opcoes_departamento = (
		('DEPTO ADMINISTRATIVO', 'DEPTO ADMINISTRATIVO'),
		('DEPTO DA CENTRAL DE SERVICOS', 'DEPTO DA CENTRAL DE SERVICOS'), 
		('DEPTO DE ATENDIMENTO E SUPORTE', 'DEPTO DE ATENDIMENTO E SUPORTE'),
		('DEPTO DE CONTRATOS', 'DEPTO DE CONTRATOS'),
		('DEPTO DE DESENVOLVIMENTO', 'DEPTO DE DESENVOLVIMENTO'),
		('DEPTO DE ENGENHARIA DE PRODUCAO', 'DEPTO DE ENGENHARIA DE PRODUCAO'), 
		('DEPTO DE NOVOS NEGOCIOS', 'DEPTO DE NOVOS NEGOCIOS'), 
		('DEPTO DE OPERACOES DE SERVICOS', 'DEPTO DE OPERACOES DE SERVICOS'), 
		('DEPTO DE PROCESSOS INTERNOS', 'DEPTO DE PROCESSOS INTERNOS'), 
		('DEPTO DE PROJETOS', 'DEPTO DE PROJETOS'), 
		('DEPTO DE PROJETOS DE OPERACOES', 'DEPTO DE PROJETOS DE OPERACOES'), 
		('DEPTO DE RECURSOS HUMANOS', 'DEPTO DE RECURSOS HUMANOS'),
		('DEPTO DE SERVICOS', 'DEPTO DE SERVICOS'), 
		('DIRETOR DE OPERACOES', 'DIRETOR DE OPERACOES'), 
		('DIRETORIA ADM./FINANCEIRA', 'DIRETORIA ADM./FINANCEIRA'),
		('FINANCEIRO/CONTABIL', 'FINANCEIRO/CONTABIL'), 
		('GERENCIA DE NOVOS SERVICOS', 'GERENCIA DE NOVOS SERVICOS'),
		('GERENCIA DE PROCESSOS E QUALIDADE(GPQ)', 'GERENCIA DE PROCESSOS E QUALIDADE(GPQ)'), 
		('GERENCIA DE PROJETOS E SOLUCOES (GPS)', 'GERENCIA DE PROJETOS E SOLUCOES (GPS)'),
		('GERENCIA DE SERVICOS REGULADOS', 'GERENCIA DE SERVICOS REGULADOS'), 
		('GERENCIA DE SUPORTE E SERVICOS (GSS)', 'GERENCIA DE SUPORTE E SERVICOS (GSS)'), 
		('JURIDICO', 'JURIDICO'),
		('NEGOCIOS', 'NEGOCIOS'),
		('PRESIDENCIA', 'PRESIDENCIA'),
		('PRODUCAO', 'PRODUCAO'), 
		('TEC.INFORMACAO', 'TEC.INFORMACAO')	
	)
	departamento = models.CharField(u'Departamento', max_length=155, choices=opcoes_departamento,   blank=False, null=False, unique=True)
	def __str__(self):
		return '%s' % (self.departamento)
	class Meta:
		verbose_name = 'Departamento'
		verbose_name_plural = 'Departamentos'
		
class Funcao(models.Model):
	id = models.AutoField(primary_key=True)
	opcoes_funcao = (
		('ADVOGADO JR', 'ADVOGADO JR'),
		('AN CONTROLADORIA SR', 'AN CONTROLADORIA SR'),
		('ANAL SUP JR - N. I', 'ANAL SUP JR - N. I'),
		('ANAL SUP PL - N. I', 'ANAL SUP PL - N. I'),
		('ANAL.CONT.FISC JR', 'ANAL.CONT.FISC JR'),
		('ANAL.DE MARKETING PL', 'ANAL.DE MARKETING PL'),
		('ANAL.SUP JR - N. II', 'ANAL.SUP JR - N. II'),
		('ANAL.SUP. PL - N. II', 'ANAL.SUP. PL - N. II'),
		('ANALIST COMERCIAL SR', 'ANALIST COMERCIAL SR'),
		('ANALISTA DE BANCO DE DADOS SR', 'ANALISTA DE BANCO DE DADOS SR'),		
		('ANALISTA DE SIST. PL', 'ANALISTA DE SIST. PL'),
		('ANALISTA DE SIST. SR', 'ANALISTA DE SIST. SR'),
		('ANALISTA DE TESTE JR', 'ANALISTA DE TESTE JR'),
		('ANALISTA DE TI PL', 'ANALISTA DE TI PL'),
		('ANALISTA DE TI SR', 'ANALISTA DE TI SR'),		
		('ANALISTA DESENV.JR', 'ANALISTA DESENV.JR'),
		('ANALISTA DESENV.PL', 'ANALISTA DESENV.PL'),
		('ANALISTA DESENV.SR', 'ANALISTA DESENV.SR'),
		('ANALISTA FINANC. JR', 'ANALISTA FINANC. JR'),
		('ANALISTA FINANC. PL', 'ANALISTA FINANC. PL'),
		('ANALISTA FINANC. SR', 'ANALISTA FINANC. SR'),
		('ANALISTA H. DESK JR', 'ANALISTA H. DESK JR'),
		('ANALISTA INFRA PL', 'ANALISTA INFRA PL'),
		('ANALISTA NEGOCIOS PL', 'ANALISTA NEGOCIOS PL'),
		('ANALISTA NEGOCIOS SR', 'ANALISTA NEGOCIOS SR'),		
		('ANALISTA PROC. PL', 'ANALISTA PROC. PL'),
		('ANALISTA PRODUC. SR', 'ANALISTA PRODUC. SR'),
		('ANALISTA PRODUC.JR', 'ANALISTA PRODUC.JR'),
		('ANALISTA PRODUC.PL', 'ANALISTA PRODUC.PL'),
		('ANALISTA PRODUT.SR', 'ANALISTA PRODUT.SR'),
		('ANALISTA PROJ. PL', 'ANALISTA PROJ. PL'),
		('ANALISTA PROJ. SR', 'ANALISTA PROJ. SR'),
		('ANALISTA RH JR', 'ANALISTA RH JR'),
		('ANALISTA RH PL', 'ANALISTA RH PL'),
		('ASSIST DIRETORIA EXE', 'ASSIST DIRETORIA EXE'),
		('ASSIST.DE DESENV.SIS', 'ASSIST.DE DESENV.SIS'),
		('AUX.ADMINISTRATIVO', 'AUX.ADMINISTRATIVO'),
		('AUXILIAR DE SUPORTE', 'AUXILIAR DE SUPORTE'),
		('CONS. DESENVOLVEDOR', 'CONS. DESENVOLVEDOR'),
		('CONS. INTERCONEXAO', 'CONS. INTERCONEXAO'),
		('CONS. SERV. SUPORTE', 'CONS. SERV. SUPORTE'),
		('CONS. SERV. SUPORTE', 'CONS. SERV. SUPORTE'),
		('CONSULTOR SIST. TI', 'CONSULTOR SIST. TI'),
		('COORD DE SISTEMAS', 'COORD DE SISTEMAS'),
		('COORD SERVICOS T.I.', 'COORD SERVICOS T.I.'),
		('COORD. DE PROJETOS', 'COORD. DE PROJETOS'),
		('COORD. TEC. INFORM.', 'COORD. TEC. INFORM.'),
		('COORDENADOR FISCAL' , 'COORDENADOR FISCAL'),
		('COORDENADOR SUPORTE', 'COORDENADOR SUPORTE'),
		('DIRETOR COMERCIAL', 'DIRETOR COMERCIAL'),
		('DIRETOR DE OPERACOES', 'DIRETOR DE OPERACOES'),
		('ESPEC DES.SISTEMAS', 'ESPEC DES.SISTEMAS'),
		('ESTAGIARIO', 'ESTAGIARIO'),
		('GER PROC E QUALIDADE', 'GER PROC E QUALIDADE'),
		('GER PROJ E SOLUCOES', 'GER PROJ E SOLUCOES'),
		('GER SUP E SERVICOS', 'GER SUP E SERVICOS'),
		('GER.CONT.INT.E COMPL', 'GER.CONT.INT.E COMPL'),
		('GER.TEC. INFORMACAO', 'GER.TEC. INFORMACAO'),
		('GERENTE DE CONTAS"', 'GERENTE DE CONTAS')	
	)
	funcao = models.CharField(u'Fun????o', max_length=155, choices=opcoes_funcao, blank=False, null=False, unique=True)
	contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)
	departamento = models.ForeignKey(Departamento,  on_delete=models.CASCADE)
	valor_hora = models.DecimalField(u'Valor Hora', max_digits=10, decimal_places=2, default='150')
	def __str__(self):
		return '%s' % (self.funcao)
	class Meta:
		verbose_name = 'Fun????o'
		verbose_name_plural = 'Fun????es'


	

