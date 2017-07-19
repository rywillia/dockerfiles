FROM fedora:latest
RUN dnf install -y wget git python && dnf clean all
RUN wget -O oc.tar.gz https://github.com/openshift/origin/releases/download/\
v1.5.0/openshift-origin-client-tools-v1.5.0-031cbe4-linux-64bit.tar.gz && tar \
xvf oc.tar.gz && rm oc.tar.gz && mv openshift-*/oc /usr/bin \
&& rm -rf openshift-*
ENTRYPOINT ["oc"]
