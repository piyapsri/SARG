CREATE TABLE `painel_falhas_em_aberto_logstash` (
  `data_coleta` datetime DEFAULT NULL,
  `numero_ocorrencia` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `titulo` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `data_criacao` date DEFAULT NULL,
  `grupo_suporte` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `tipo_servico` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  UNIQUE KEY `numero_ocorrencia` (`numero_ocorrencia`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci  
;
CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`%` 
    SQL SECURITY DEFINER
VIEW `vw_painel_falhas_em_aberto_logstash` AS
    SELECT 
        `painel_falhas_em_aberto_logstash`.`data_coleta` AS `data_coleta`,
        `painel_falhas_em_aberto_logstash`.`numero_ocorrencia` AS `numero_ocorrencia`,
        `painel_falhas_em_aberto_logstash`.`titulo` AS `titulo`,
        `painel_falhas_em_aberto_logstash`.`data_criacao` AS `data_criacao`,
        `painel_falhas_em_aberto_logstash`.`grupo_suporte` AS `grupo_suporte`,
        `painel_falhas_em_aberto_logstash`.`tipo_servico` AS `tipo_servico`
    FROM
        `painel_falhas_em_aberto_logstash`
    WHERE
        (`painel_falhas_em_aberto_logstash`.`data_coleta` = (SELECT 
                MAX(`painel_falhas_em_aberto_logstash`.`data_coleta`)
            FROM
                `painel_falhas_em_aberto_logstash`))
;
CREATE TABLE `painel_ocorrencias_abertas_no_mes_logstash` (
  `data_coleta` datetime DEFAULT NULL,
  `numero_ocorrencia` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `titulo` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `data_criacao` date DEFAULT NULL,
  `data_solucao` date DEFAULT NULL,
  `grupo_suporte` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `tipo_servico` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  UNIQUE KEY `numero_ocorrencia` (`numero_ocorrencia`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
;
CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`%` 
    SQL SECURITY DEFINER
VIEW `vw_painel_ocorrencias_abertas_no_mes_logstash` AS
    SELECT 
        `painel_ocorrencias_abertas_no_mes_logstash`.`data_coleta` AS `data_coleta`,
        `painel_ocorrencias_abertas_no_mes_logstash`.`numero_ocorrencia` AS `numero_ocorrencia`,
        `painel_ocorrencias_abertas_no_mes_logstash`.`titulo` AS `titulo`,
        `painel_ocorrencias_abertas_no_mes_logstash`.`data_criacao` AS `data_criacao`,
        `painel_ocorrencias_abertas_no_mes_logstash`.`data_solucao` AS `data_solucao`,
        `painel_ocorrencias_abertas_no_mes_logstash`.`grupo_suporte` AS `grupo_suporte`,
        `painel_ocorrencias_abertas_no_mes_logstash`.`tipo_servico` AS `tipo_servico`
    FROM
        `painel_ocorrencias_abertas_no_mes_logstash`
    WHERE
        (`painel_ocorrencias_abertas_no_mes_logstash`.`data_coleta` = (SELECT 
                MAX(`painel_ocorrencias_abertas_no_mes_logstash`.`data_coleta`)
            FROM
                `painel_ocorrencias_abertas_no_mes_logstash`))
;
CREATE TABLE `painel_ocorrencias_em_aberto_logstash` (
  `data_coleta` datetime DEFAULT NULL,
  `numero_ocorrencia` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `titulo` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `data_criacao` date DEFAULT NULL,
  `grupo_suporte` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `tipo_servico` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `situacao` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  UNIQUE KEY `numero_ocorrencia` (`numero_ocorrencia`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
;
CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`%` 
    SQL SECURITY DEFINER
VIEW `vw_painel_ocorrencias_em_aberto_logstash` AS
    SELECT 
        `painel_ocorrencias_em_aberto_logstash`.`data_coleta` AS `data_coleta`,
        `painel_ocorrencias_em_aberto_logstash`.`numero_ocorrencia` AS `numero_ocorrencia`,
        `painel_ocorrencias_em_aberto_logstash`.`titulo` AS `titulo`,
        `painel_ocorrencias_em_aberto_logstash`.`data_criacao` AS `data_criacao`,
        `painel_ocorrencias_em_aberto_logstash`.`grupo_suporte` AS `grupo_suporte`,
        `painel_ocorrencias_em_aberto_logstash`.`tipo_servico` AS `tipo_servico`,
        `painel_ocorrencias_em_aberto_logstash`.`situacao` AS `situacao`
    FROM
        `painel_ocorrencias_em_aberto_logstash`
    WHERE
        (`painel_ocorrencias_em_aberto_logstash`.`data_coleta` = (SELECT 
                MAX(`painel_ocorrencias_em_aberto_logstash`.`data_coleta`)
            FROM
                `painel_ocorrencias_em_aberto_logstash`))
; 
CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`%` 
    SQL SECURITY DEFINER
VIEW `vw_painel_ocorrencias_em_aberto_graph` AS
    SELECT 
        `a`.`servico` AS `SERVICO`,
        (SELECT 
                IFNULL(SUM(`b`.`quantidade`), 0)
            FROM
                (SELECT 
                    COUNT(0) AS `quantidade`,
                        `a`.`tipo_servico` AS `servico`,
                        `a`.`situacao` AS `situacao`
                FROM
                    `sarg`.`vw_painel_ocorrencias_em_aberto_logstash` `a`
                GROUP BY `a`.`tipo_servico` , `a`.`situacao`) `b`
            WHERE
                ((`b`.`servico` = `a`.`servico`)
                    AND (`b`.`situacao` = 'Aguardando o solicitante'))) AS `AGUARDANDO`,
        (SELECT 
                IFNULL(SUM(`c`.`quantidade`), 0)
            FROM
                (SELECT 
                    COUNT(0) AS `quantidade`,
                        `a`.`tipo_servico` AS `servico`,
                        `a`.`situacao` AS `situacao`
                FROM
                    `sarg`.`vw_painel_ocorrencias_em_aberto_logstash` `a`
                GROUP BY `a`.`tipo_servico` , `a`.`situacao`) `c`
            WHERE
                ((`c`.`servico` = `a`.`servico`)
                    AND (`c`.`situacao` = 'Em atendimento'))) AS `ATENDIMENTO`,
        (SELECT 
                IFNULL(SUM(`c`.`quantidade`), 0)
            FROM
                (SELECT 
                    COUNT(0) AS `quantidade`,
                        `a`.`tipo_servico` AS `servico`,
                        `a`.`situacao` AS `situacao`
                FROM
                    `sarg`.`vw_painel_ocorrencias_em_aberto_logstash` `a`
                GROUP BY `a`.`tipo_servico` , `a`.`situacao`) `c`
            WHERE
                ((`c`.`servico` = `a`.`servico`)
                    AND (`c`.`situacao` = 'Encaminhada'))) AS `ENCAMINHADO`,
        (SELECT 
                IFNULL(SUM(`d`.`quantidade`), 0)
            FROM
                (SELECT 
                    COUNT(0) AS `quantidade`,
                        `a`.`tipo_servico` AS `servico`,
                        `a`.`situacao` AS `situacao`
                FROM
                    `sarg`.`vw_painel_ocorrencias_em_aberto_logstash` `a`
                GROUP BY `a`.`tipo_servico` , `a`.`situacao`) `d`
            WHERE
                ((`d`.`servico` = `a`.`servico`)
                    AND (`d`.`situacao` IN ('Aguardando o solicitante' , 'Em atendimento', 'Encaminhada')))) AS `TOTAL`
    FROM
        (SELECT 
            COUNT(0) AS `quantidade`,
                `a`.`tipo_servico` AS `servico`,
                `a`.`situacao` AS `situacao`
        FROM
            `sarg`.`vw_painel_ocorrencias_em_aberto_logstash` `a`
        GROUP BY `a`.`tipo_servico` , `a`.`situacao`) `a`
    GROUP BY `a`.`servico`
    ORDER BY `TOTAL` DESC
    
;
CREATE TABLE `painel_falhas_encerredas_nos_ultimos_6_meses_logstash` (
  `data_coleta` datetime DEFAULT NULL,
  `numero_ocorrencia` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `titulo` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `data_criacao` date DEFAULT NULL,
  `data_solucao` date DEFAULT NULL,
  `grupo_suporte` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `tipo_servico` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `situacao` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  UNIQUE KEY `numero_ocorrencia` (`numero_ocorrencia`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
;

CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`%` 
    SQL SECURITY DEFINER
VIEW `vw_painel_falhas_encerredas_nos_ultimos_6_meses_logstash` AS
    SELECT 
        `painel_falhas_encerredas_nos_ultimos_6_meses_logstash`.`data_coleta` AS `data_coleta`,
        `painel_falhas_encerredas_nos_ultimos_6_meses_logstash`.`numero_ocorrencia` AS `numero_ocorrencia`,
        `painel_falhas_encerredas_nos_ultimos_6_meses_logstash`.`titulo` AS `titulo`,
        `painel_falhas_encerredas_nos_ultimos_6_meses_logstash`.`data_criacao` AS `data_criacao`,
        `painel_falhas_encerredas_nos_ultimos_6_meses_logstash`.`data_solucao` AS `data_solucao`,
        `painel_falhas_encerredas_nos_ultimos_6_meses_logstash`.`grupo_suporte` AS `grupo_suporte`,
        `painel_falhas_encerredas_nos_ultimos_6_meses_logstash`.`tipo_servico` AS `tipo_servico`,
        `painel_falhas_encerredas_nos_ultimos_6_meses_logstash`.`situacao` AS `situacao`
    FROM
        `painel_falhas_encerredas_nos_ultimos_6_meses_logstash`
    WHERE
        (`painel_falhas_encerredas_nos_ultimos_6_meses_logstash`.`data_coleta` = (SELECT 
                MAX(`painel_falhas_encerredas_nos_ultimos_6_meses_logstash`.`data_coleta`)
            FROM
                `painel_falhas_encerredas_nos_ultimos_6_meses_logstash`))             
;


CREATE TABLE `painel_demandas_logstash` (
  `consulta` datetime DEFAULT NULL,
  `numero_ocorrencia` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `titulo` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `data_criacao` date DEFAULT NULL,
  `data_solucao` date DEFAULT NULL,
  `grupo_suporte` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `tipo_servico` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `situacao` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `severidade` varchar(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `responsavel` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `tipo` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `servico` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `horas_previstas` int(11) DEFAULT NULL,
  `qtde_hrs_realizada` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  UNIQUE KEY `numero_ocorrencia` (`numero_ocorrencia`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
;
CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`%` 
    SQL SECURITY DEFINER
VIEW `sarg`.`vw_painel_demandas_logstash` AS
    SELECT 
        `sarg`.`painel_demandas_logstash`.`consulta` AS `consulta`,
        `sarg`.`painel_demandas_logstash`.`numero_ocorrencia` AS `numero_ocorrencia`,
        `sarg`.`painel_demandas_logstash`.`titulo` AS `titulo`,
        `sarg`.`painel_demandas_logstash`.`data_criacao` AS `data_criacao`,
        `sarg`.`painel_demandas_logstash`.`data_solucao` AS `data_solucao`,
        `sarg`.`painel_demandas_logstash`.`grupo_suporte` AS `grupo_suporte`,
        `sarg`.`painel_demandas_logstash`.`tipo_servico` AS `tipo_servico`,
        `sarg`.`painel_demandas_logstash`.`situacao` AS `situacao`,
        `sarg`.`painel_demandas_logstash`.`severidade` AS `severidade`,
        `sarg`.`painel_demandas_logstash`.`responsavel` AS `responsavel`,
        `sarg`.`painel_demandas_logstash`.`tipo` AS `tipo`,
        `sarg`.`painel_demandas_logstash`.`servico` AS `servico`,  
        `sarg`.`painel_demandas_logstash`.`horas_previstas` AS `horas_previstas`,
        `sarg`.`painel_demandas_logstash`.`qtde_hrs_realizada` AS `qtde_hrs_realizada`
              
    FROM
        `sarg`.`painel_demandas_logstash`
    WHERE
        (`sarg`.`painel_demandas_logstash`.`consulta` = (SELECT 
                MAX(`sarg`.`painel_demandas_logstash`.`consulta`)
            FROM
                `sarg`.`painel_demandas_logstash`))

;
CREATE TABLE `painel_ocorrencias_encerradas_no_mes_atual_logstash` (
  `data_coleta` datetime DEFAULT NULL,
  `numero_ocorrencia` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `titulo` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `data_criacao` date DEFAULT NULL,
  `data_solucao` date DEFAULT NULL,
  `grupo_suporte` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `tipo_servico` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  UNIQUE KEY `numero_ocorrencia` (`numero_ocorrencia`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci    
    
 ;   
CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`%` 
    SQL SECURITY DEFINER
VIEW `vw_painel_ocorrencias_encerradas_no_mes_atual_logstash` AS
    SELECT 
        `painel_ocorrencias_encerradas_no_mes_atual_logstash`.`data_coleta` AS `data_coleta`,
        `painel_ocorrencias_encerradas_no_mes_atual_logstash`.`numero_ocorrencia` AS `numero_ocorrencia`,
        `painel_ocorrencias_encerradas_no_mes_atual_logstash`.`titulo` AS `titulo`,
        `painel_ocorrencias_encerradas_no_mes_atual_logstash`.`data_criacao` AS `data_criacao`,
        `painel_ocorrencias_encerradas_no_mes_atual_logstash`.`data_solucao` AS `data_solucao`,
        `painel_ocorrencias_encerradas_no_mes_atual_logstash`.`grupo_suporte` AS `grupo_suporte`,
        `painel_ocorrencias_encerradas_no_mes_atual_logstash`.`tipo_servico` AS `tipo_servico`
    FROM
        `painel_ocorrencias_encerradas_no_mes_atual_logstash`
    WHERE
        (`painel_ocorrencias_encerradas_no_mes_atual_logstash`.`data_coleta` = (SELECT 
                MAX(`painel_ocorrencias_encerradas_no_mes_atual_logstash`.`data_coleta`)
            FROM
                `painel_ocorrencias_encerradas_no_mes_atual_logstash`))
;     




CREATE TABLE `painel_rateio_horas_por_pessoa_logstash` (
  `id_func` int(100) NOT NULL,
  `nome` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `semana_1` varchar(13) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `semana_2` varchar(13) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `semana_3` varchar(13) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `semana_4` varchar(13) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `semana_5` varchar(13) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `estatus` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `periodo` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ultima_semana_periodo` int(11) DEFAULT NULL,
  `EMAIL` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  UNIQUE KEY `id_func` (`id_func`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci


;
CREATE TABLE `painel_rateio_horas_por_ic_ativ_logstash` (
  `id_tipo` int(11) DEFAULT NULL,
  `descricao` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `descricao_atividade` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `id_ic` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `descricao_ic` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `periodo` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `qtd_horas` decimal(20,0) DEFAULT NULL,
  `id_atividade` int(11) DEFAULT NULL,
  UNIQUE KEY `id_tipo` (`id_tipo`,`descricao`,`qtd_horas`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
;



CREATE TABLE `painel_orcamentos_logstash` (
  `periodo` varchar(6) DEFAULT NULL,
  `grupo_despesa` varchar(255) DEFAULT NULL,
  `cod_natureza` int(11) DEFAULT NULL,
  `descricao_natureza` varchar(30) DEFAULT NULL,
  `centro_custo` varchar(5) DEFAULT NULL,
  `item_contabil` varchar(5) DEFAULT NULL,
  `descricao_item` varchar(40) DEFAULT NULL,
  `valor_aprovado` float(20,2) DEFAULT NULL,
  `valor_acumulado_mes` float(20,2) DEFAULT NULL,
  UNIQUE KEY `uniq_periodo_custo_contabil` (`periodo`,`centro_custo`,`item_contabil`,`cod_natureza`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
;

CREATE TABLE `painel_ongoing_ongoing` (
  `item_contabil` varchar(5) NOT NULL,
  `descricao_item_contabil` varchar(500) DEFAULT NULL,
  `hora_100_pc` int(11) DEFAULT NULL,
  `hora_75_pc` int(11) DEFAULT NULL,
  `hora_normal` int(11) DEFAULT NULL,
  `hora_total` int(11) DEFAULT NULL,
  `des_atividade` varchar(500) DEFAULT NULL,
  `cod_atividade` int(11) NOT NULL,
  `periodo` varchar(15) NOT NULL,
  UNIQUE KEY `IX_IC_ONGOING` (`item_contabil`,`cod_atividade`,`periodo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1


;

CREATE TABLE `painel_projetos_e_oportunidaes_ic_x_horas_logstash` (
  `ITEM_CONTABIL` varchar(255) DEFAULT NULL,
  `DESCRICAO` varchar(255) DEFAULT NULL,
  `COD_ATIVIDADE` int(11) DEFAULT NULL,
  `DESC_ATIVIDADE` varchar(255) DEFAULT NULL,
  `HORAS_ARREND` varchar(255) DEFAULT NULL,
  UNIQUE KEY `UNIQUE_IC` (`ITEM_CONTABIL`,`COD_ATIVIDADE`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1
;
delimiter $$

CREATE DEFINER=`root`@`%` FUNCTION `FN_FORMATA_HORA`( VALOR DECIMAL(13,6), RETORNO CHAR(1) ) RETURNS varchar(15) CHARSET utf8mb4 COLLATE utf8mb4_unicode_ci
BEGIN
     
     DECLARE INT_VAL, DEC_VAL INTEGER;
     
     DECLARE RESULTADO VARCHAR(15);
     
     SET INT_VAL = FLOOR(VALOR);
     
     SET DEC_VAL = FLOOR((VALOR - INT_VAL) * 60);
	
     IF RETORNO = 'H' THEN
		SET RESULTADO = INT_VAL;
     ELSE
		SET RESULTADO = CONCAT((INT_VAL), ':', LPAD(DEC_VAL, 2, "0"));
     END IF;
     
 	RETURN RESULTADO;
     
 END$$
 ;
