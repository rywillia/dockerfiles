#
# A example dockerfile used to create an image with a basic flask application
# This was image was needed to test openshift origin.
#
FROM fedora:latest

# Install required packages
RUN dnf install -y python python-pip
RUN pip install flask

# Copy python file to the image filesystem
ADD app.py /

# Expose port 5000
EXPOSE 5000

# Run the flask application
CMD [ "/usr/bin/python", "/app.py" ]
