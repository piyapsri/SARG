for email in `sudo docker exec mysql /usr/bin/mysql --login-path=local -h mysql -uroot -proot mars -e "select email from painel_rateio_horas_logstash where estatus = 'ATRASADO'" -s -N 2> /dev/null`
do
echo "
Content-type: text/plain; charset=UTF-8
To: ${email}
Cc: fsaito@cleartech.com.br, apessoa@cleartech.com.br, dpossebon@cleartech.com.br
Subject: SARG - Pend�ncia(s) Rateio(s) E-ponto.


Prezado(a),

Foi identificado que voc� possui rateio(s) de marca��o de ponto(s) pendente(s). h� mais de 2 semanas.

� poss�vel visualizar as pend�ncias no SARG pela URL: http://sarg.cleartech.com.br/painel_rateio_horas/rateio

Favor, regularizar seus rateios no e-ponto atrav�s da URL: http://eponto.cleartech.com.br/epontoweb/Login.aspx

Atenciosamente,
Coordena��o GNS


" > mail.txt
sendmail $email < mail.txt
done
