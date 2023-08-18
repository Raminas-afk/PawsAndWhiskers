# Use the official Python image as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required packages
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Specify the command to start the Celery worker
CMD ["celery", "-A", "pawsandwhiskers.celery", "worker", "--loglevel=info", "-P", "eventlet"]


