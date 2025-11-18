# content of the Dockerfile
# Python 3.10 as base image
FROM python:3.10

# Copy requirements file into the image
COPY requirements.txt /

# Install dependencies
RUN pip install -r /requirements.txt

# Copy the rest of the application code
COPY . /app

# Set the working directory
WORKDIR /app

# Expose the gateway port
EXPOSE 5001

# Run the gateway application
CMD ["python", "application.py"]
