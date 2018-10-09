for email in `sudo docker exec mysql /usr/bin/mysql --login-path=local -h mysql -uroot -proot mars -e "select email from painel_rateio_horas_logstash where estatus = 'ATRASADO'" -s -N 2> /dev/null`
do
echo "
Content-type: text/plain; charset=UTF-8
To: ${email}
Cc: fsaito@cleartech.com.br, apessoa@cleartech.com.br, dpossebon@cleartech.com.br
Subject: SARG - Pendência(s) Rateio(s) E-ponto.


Prezado(a),

Foi identificado que você possui rateio(s) de marcação de ponto(s) pendente(s). há mais de 2 semanas.

É possível visualizar as pendências no SARG pela URL: http://sarg.cleartech.com.br/painel_rateio_horas/rateio

Favor, regularizar seus rateios no e-ponto através da URL: http://eponto.cleartech.com.br/epontoweb/Login.aspx

Atenciosamente,
Coordenação GNS


" > mail.txt
sendmail $email < mail.txt
done
