# SARG
Sistema de Análise e Relatórios de Gestão

SARG is opensource software.

http://sarg.readthedocs.io for latest documentation

This project contains the following modules.

<ul>
  <li>login</li>
  <li>painel_bugs</li>
  <li>painel_demandas</li>
  <li>painel_incidentes</li>
  <li>painel_orcamentos</li>
  <li>painel_oportunidades</li>
  <li>painel_monitoracoes</li>
  <li>painel_gmuds</li>
  <li>painel_rateio_horas</li>
  <li>painel_projetos</li>
  <li>painel_ongoing</li>
  <li>clientes</li>
  <li>cadastro_financeiro</li>
  <li>painel_horas_gns</li>
  <li>receitas_extras_ongoing</li>
  <li>funcionarios</li>
</ul>

<h2>Installation - Requirements</h2>

<h3>Docker containers/versions:</h3>

<ul>
  <li>python:3.7.0</li>
  <li>mysqld 5.7</li>
  <li>logstash-oss:6.2.1</li>
  <li>nginx:1.15.2</li>
</ul>

<h3>Python (pip) packages/versions requirements:</h3>

<ul>  
  <li>django==2.1.0</li>
  <li>gunicorn==19.9.0</li>
  <li>mysqlclient==1.3.13</li>
  <li>Pillow==5.2.0</li>
</ul>

<h2>Creating Tables, Views and Functions for SARG</h2>

<pre>
sudo docker exec -it mysql bash
mysql -uroot -p sarg < /tmp/generateTablesViewsSarg.sql
Enter password:
ERROR 1065 (42000) at line 381: Query was empty
root@bb77ac860c80:/#
</pre>


<h2>Creating Super User Django Admin</h2>

<pre>
sudo docker exec -it sarg sh
python manage.py createsuperuser 
</pre>

<h2>Creating Tables, Views and Functions on Mysql</h2>
<pre>
sudo docker exec -it sarg sh
python manage.py createsuperuser 
</pre>
