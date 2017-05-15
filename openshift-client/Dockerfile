#
# Openshift origin client tool (v1.5.0)
#
FROM fedora:latest

# Install required packages
RUN dnf install -y git wget python

# Download openshift origin client tool
RUN wget -O /tmp/openshift-client.tar.gz https://github.com/openshift/origin/\
releases/download/v1.5.0/openshift-origin-client-tools-v1.5.0-031cbe4-\
linux-64bit.tar.gz

# Extract openshift origin client tool
RUN cd /tmp; tar -xvf openshift-client.tar.gz;

# Move the openshift origin client tool to the system binary path
RUN mv /tmp/openshift-*/oc /usr/bin

# Run the openshift origin client tool
ENTRYPOINT ["oc"]