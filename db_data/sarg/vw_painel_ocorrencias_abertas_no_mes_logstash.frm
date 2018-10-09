TYPE=VIEW
query=select `sarg`.`painel_ocorrencias_abertas_no_mes_logstash`.`data_coleta` AS `data_coleta`,`sarg`.`painel_ocorrencias_abertas_no_mes_logstash`.`numero_ocorrencia` AS `numero_ocorrencia`,`sarg`.`painel_ocorrencias_abertas_no_mes_logstash`.`titulo` AS `titulo`,`sarg`.`painel_ocorrencias_abertas_no_mes_logstash`.`data_criacao` AS `data_criacao`,`sarg`.`painel_ocorrencias_abertas_no_mes_logstash`.`data_solucao` AS `data_solucao`,`sarg`.`painel_ocorrencias_abertas_no_mes_logstash`.`grupo_suporte` AS `grupo_suporte`,`sarg`.`painel_ocorrencias_abertas_no_mes_logstash`.`tipo_servico` AS `tipo_servico` from `sarg`.`painel_ocorrencias_abertas_no_mes_logstash` where (`sarg`.`painel_ocorrencias_abertas_no_mes_logstash`.`data_coleta` = (select max(`sarg`.`painel_ocorrencias_abertas_no_mes_logstash`.`data_coleta`) from `sarg`.`painel_ocorrencias_abertas_no_mes_logstash`))
md5=594266752f292ad68b12aca8a6f82b49
updatable=0
algorithm=0
definer_user=root
definer_host=%
suid=1
with_check_option=0
timestamp=2018-10-09 15:22:19
create-version=1
source=SELECT \n        `painel_ocorrencias_abertas_no_mes_logstash`.`data_coleta` AS `data_coleta`,\n        `painel_ocorrencias_abertas_no_mes_logstash`.`numero_ocorrencia` AS `numero_ocorrencia`,\n        `painel_ocorrencias_abertas_no_mes_logstash`.`titulo` AS `titulo`,\n        `painel_ocorrencias_abertas_no_mes_logstash`.`data_criacao` AS `data_criacao`,\n        `painel_ocorrencias_abertas_no_mes_logstash`.`data_solucao` AS `data_solucao`,\n        `painel_ocorrencias_abertas_no_mes_logstash`.`grupo_suporte` AS `grupo_suporte`,\n        `painel_ocorrencias_abertas_no_mes_logstash`.`tipo_servico` AS `tipo_servico`\n    FROM\n        `painel_ocorrencias_abertas_no_mes_logstash`\n    WHERE\n        (`painel_ocorrencias_abertas_no_mes_logstash`.`data_coleta` = (SELECT \n                MAX(`painel_ocorrencias_abertas_no_mes_logstash`.`data_coleta`)\n            FROM\n                `painel_ocorrencias_abertas_no_mes_logstash`))
client_cs_name=latin1
connection_cl_name=latin1_swedish_ci
view_body_utf8=select `sarg`.`painel_ocorrencias_abertas_no_mes_logstash`.`data_coleta` AS `data_coleta`,`sarg`.`painel_ocorrencias_abertas_no_mes_logstash`.`numero_ocorrencia` AS `numero_ocorrencia`,`sarg`.`painel_ocorrencias_abertas_no_mes_logstash`.`titulo` AS `titulo`,`sarg`.`painel_ocorrencias_abertas_no_mes_logstash`.`data_criacao` AS `data_criacao`,`sarg`.`painel_ocorrencias_abertas_no_mes_logstash`.`data_solucao` AS `data_solucao`,`sarg`.`painel_ocorrencias_abertas_no_mes_logstash`.`grupo_suporte` AS `grupo_suporte`,`sarg`.`painel_ocorrencias_abertas_no_mes_logstash`.`tipo_servico` AS `tipo_servico` from `sarg`.`painel_ocorrencias_abertas_no_mes_logstash` where (`sarg`.`painel_ocorrencias_abertas_no_mes_logstash`.`data_coleta` = (select max(`sarg`.`painel_ocorrencias_abertas_no_mes_logstash`.`data_coleta`) from `sarg`.`painel_ocorrencias_abertas_no_mes_logstash`))
