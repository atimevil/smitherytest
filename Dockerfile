# Dockerfile
# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Install pip and required packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Command to run the application (overridden by smithery.yaml but good practice)
CMD ["python", "-u", "server.py"]

# Expose the port (FastMCP listens on 8000)
EXPOSE 8000
