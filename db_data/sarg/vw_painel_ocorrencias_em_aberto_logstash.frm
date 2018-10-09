TYPE=VIEW
query=select `sarg`.`painel_ocorrencias_em_aberto_logstash`.`data_coleta` AS `data_coleta`,`sarg`.`painel_ocorrencias_em_aberto_logstash`.`numero_ocorrencia` AS `numero_ocorrencia`,`sarg`.`painel_ocorrencias_em_aberto_logstash`.`titulo` AS `titulo`,`sarg`.`painel_ocorrencias_em_aberto_logstash`.`data_criacao` AS `data_criacao`,`sarg`.`painel_ocorrencias_em_aberto_logstash`.`grupo_suporte` AS `grupo_suporte`,`sarg`.`painel_ocorrencias_em_aberto_logstash`.`tipo_servico` AS `tipo_servico`,`sarg`.`painel_ocorrencias_em_aberto_logstash`.`situacao` AS `situacao` from `sarg`.`painel_ocorrencias_em_aberto_logstash` where (`sarg`.`painel_ocorrencias_em_aberto_logstash`.`data_coleta` = (select max(`sarg`.`painel_ocorrencias_em_aberto_logstash`.`data_coleta`) from `sarg`.`painel_ocorrencias_em_aberto_logstash`))
md5=191db9396ce6c42dbb77056d4fe7e9bb
updatable=0
algorithm=0
definer_user=root
definer_host=%
suid=1
with_check_option=0
timestamp=2018-10-09 15:22:19
create-version=1
source=SELECT \n        `painel_ocorrencias_em_aberto_logstash`.`data_coleta` AS `data_coleta`,\n        `painel_ocorrencias_em_aberto_logstash`.`numero_ocorrencia` AS `numero_ocorrencia`,\n        `painel_ocorrencias_em_aberto_logstash`.`titulo` AS `titulo`,\n        `painel_ocorrencias_em_aberto_logstash`.`data_criacao` AS `data_criacao`,\n        `painel_ocorrencias_em_aberto_logstash`.`grupo_suporte` AS `grupo_suporte`,\n        `painel_ocorrencias_em_aberto_logstash`.`tipo_servico` AS `tipo_servico`,\n        `painel_ocorrencias_em_aberto_logstash`.`situacao` AS `situacao`\n    FROM\n        `painel_ocorrencias_em_aberto_logstash`\n    WHERE\n        (`painel_ocorrencias_em_aberto_logstash`.`data_coleta` = (SELECT \n                MAX(`painel_ocorrencias_em_aberto_logstash`.`data_coleta`)\n            FROM\n                `painel_ocorrencias_em_aberto_logstash`))
client_cs_name=latin1
connection_cl_name=latin1_swedish_ci
view_body_utf8=select `sarg`.`painel_ocorrencias_em_aberto_logstash`.`data_coleta` AS `data_coleta`,`sarg`.`painel_ocorrencias_em_aberto_logstash`.`numero_ocorrencia` AS `numero_ocorrencia`,`sarg`.`painel_ocorrencias_em_aberto_logstash`.`titulo` AS `titulo`,`sarg`.`painel_ocorrencias_em_aberto_logstash`.`data_criacao` AS `data_criacao`,`sarg`.`painel_ocorrencias_em_aberto_logstash`.`grupo_suporte` AS `grupo_suporte`,`sarg`.`painel_ocorrencias_em_aberto_logstash`.`tipo_servico` AS `tipo_servico`,`sarg`.`painel_ocorrencias_em_aberto_logstash`.`situacao` AS `situacao` from `sarg`.`painel_ocorrencias_em_aberto_logstash` where (`sarg`.`painel_ocorrencias_em_aberto_logstash`.`data_coleta` = (select max(`sarg`.`painel_ocorrencias_em_aberto_logstash`.`data_coleta`) from `sarg`.`painel_ocorrencias_em_aberto_logstash`))
