# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY frontend.py .

# Expose the port the app runs on
EXPOSE 3000

# Define the command to run the application
CMD ["python", "frontend.py"]
