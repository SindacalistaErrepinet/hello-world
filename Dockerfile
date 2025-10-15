# Use Python 3.12 Alpine as base image
FROM python:3.12-alpine

# Create a non-privileged user
RUN addgroup -g 1001 -S appgroup && \
    adduser -u 1001 -S appuser -G appgroup

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install gunicorn
RUN pip install --no-cache-dir gunicorn

# Copy all application code
COPY . .

# Change ownership of files to non-privileged user
RUN chown -R appuser:appgroup /app

# Switch to non-privileged user
USER appuser

# Expose port (usually 8000 for gunicorn)
EXPOSE 8000

# Command to run the application with gunicorn
CMD ["gunicorn", "--config", "gunicorn_config.py", "app"]