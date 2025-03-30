# Use Python 3.11
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend code
COPY . .

# Expose port 5000
EXPOSE 5000

# Run the backend server
CMD ["python", "app.py"]

