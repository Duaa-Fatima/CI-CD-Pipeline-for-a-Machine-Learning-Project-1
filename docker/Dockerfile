# Use Python base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy only the requirements first (for caching)
COPY ../app/requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create the necessary directories (Important!)
RUN mkdir -p /app/data

# Copy the entire app directory and data directory
COPY ../app /app
COPY ../data /app/data

# Expose Flask port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
