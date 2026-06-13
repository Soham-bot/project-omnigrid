# Use a lightweight version of Python
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy our requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy our actual application code into the container
COPY app.py .

# Tell Docker our app uses port 5000
EXPOSE 5000

# The command to run when the container starts
CMD ["python", "app.py"]
