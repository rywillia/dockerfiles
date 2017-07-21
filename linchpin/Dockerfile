FROM fedora:latest
RUN curl -o /etc/yum.repos.d/beaker-client-Fedora.repo \
https://beaker-project.org/yum/beaker-client-Fedora.repo
RUN dnf install -y beaker-client krb5-workstation python-pip gcc \
redhat-rpm-config python-devel openssl-devel && dnf clean all
RUN pip install linchpin>=1.0.0 beaker-client==23.3
ENTRYPOINT ['linchpin']