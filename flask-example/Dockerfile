FROM fedora:latest
RUN dnf install -y python python-pip
RUN pip install flask
ADD app.py /
EXPOSE 5000
CMD [ "/usr/bin/python", "/app.py" ]
