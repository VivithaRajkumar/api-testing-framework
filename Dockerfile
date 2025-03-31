# Start from a Python base image
FROM python:3.9-slim

#This ensures the entire project is available at /app within the container.
COPY . /app

#Ensure the PYTHONPATH is Set Correctly
ENV PYTHONPATH /app:$PYTHONPATH

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory content into the container at /app
COPY . /app

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

# Expose any necessary ports (optional)
EXPOSE 8080

# Command to run the tests (use pytest)
CMD ["pytest", "--maxfail=5", "--disable-warnings", "--html=report.html", "--self-contained-html"]




