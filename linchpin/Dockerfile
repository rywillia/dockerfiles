FROM fedora:latest
RUN dnf install -y python-pip gcc redhat-rpm-config python-devel\
    openssl-devel && dnf clean all
RUN pip install "linchpin>=1.0.0"