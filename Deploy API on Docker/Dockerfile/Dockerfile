# Add the contents of the Dockerfile from the task description
# Use Python 3.10 as base image
FROM python:3.10

# Copy requirements.txt into the container
COPY requirements.txt /

# Install dependencies
RUN pip install -r /requirements.txt

# Copy the rest of the application code
COPY . /app

# Set working directory inside the container
WORKDIR /app

# Expose port 5000 (Flask default)
EXPOSE 5000

# Run the API
CMD ["python", "api.py"]
