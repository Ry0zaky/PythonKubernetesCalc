# Use the official Python image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory's contents into the container
COPY . .

# Install required Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 to allow external access
EXPOSE 5000

# Run the Flask application
CMD ["python", "PythonKubernetes.py"]
