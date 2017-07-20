FROM fedora:latest
RUN dnf install -y python-pip gcc redhat-rpm-config python-devel\
    openssl-devel libxslt-python && dnf clean all
RUN pip install linchpin>=1.0.0 beaker-client==23.3 python-krbV
