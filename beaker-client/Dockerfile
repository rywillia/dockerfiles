FROM fedora:latest

# Download beaker-client repository
RUN curl -o /etc/yum.repos.d/beaker-client-Fedora.repo \
https://beaker-project.org/yum/beaker-client-Fedora.repo

# Install beaker-client and downgrade to set version (issues running latest)
RUN dnf install -y beaker-client krb5-workstation && dnf clean all
RUN pip install beaker-client==23.3

# Copy beaker conf to /etc/beaker/client.conf
RUN cp /usr/share/doc/beaker-client/client.conf.example /etc/beaker/client.conf

# Set entrypoint to beaker-client, which user can override
ENTRYPOINT ['bkr']