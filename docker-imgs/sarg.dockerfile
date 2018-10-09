FROM python:3.7.0
ENV PYTHONUNBUFFERED 1  
RUN mkdir /sarg
WORKDIR /sarg
ADD ./conf/sarg/requirements.pip /sarg
RUN pip install --no-cache-dir -r requirements.pip
ADD ./sarg /sarg

# Adicionando driver Oracle no container
ADD ./conf/sarg/drivers_databases/oracle/oracle-instantclient*.deb /tmp/

RUN echo "deb http://ftp.de.debian.org/debian jessie main" >> /etc/apt/sources.list && apt-get update && apt-get install libaio1 && dpkg -i /tmp/oracle-instantclient*.deb && rm -f /tmp/oracle-instantclient*.deb && echo /usr/lib/oracle/12.2/client64/lib > /etc/ld.so.conf.d/oracle-instantclient12.2.conf && ldconfig
ENV PATH=$PATH:/usr/lib/oracle/12.2/client64/bin
