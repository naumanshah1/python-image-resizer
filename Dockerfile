# Use official Python base image
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy all files from project folder to container's /app directory
COPY . .

# Install all Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 so we can access it
EXPOSE 5000

# Start the Flask app
CMD ["python", "app.py"]
