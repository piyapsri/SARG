# https://github.com/elastic/logstash-docker
FROM docker.elastic.co/logstash/logstash-oss:6.2.1

# Add your logstash plugins setup here
RUN logstash-plugin install logstash-output-jdbc
