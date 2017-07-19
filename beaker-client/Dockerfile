FROM fedora:latest
RUN curl -o /etc/yum.repos.d/beaker-client-Fedora.repo \
https://beaker-project.org/yum/beaker-client-Fedora.repo
RUN dnf install -y beaker-client krb5-workstation && dnf clean all
RUN pip install beaker-client==23.3
RUN cp /usr/share/doc/beaker-client/client.conf.example /etc/beaker/client.conf
ENTRYPOINT ['bkr']
