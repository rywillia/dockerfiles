FROM centos:7
RUN yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-\
latest-7.noarch.rpm
RUN yum install -y git gcc redhat-rpm-config libffi-devel openssl-devel \
python-devel python-pip
RUN pip install --upgrade pip
RUN yum clean all