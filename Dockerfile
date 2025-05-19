# Use the official Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

RUN apt update && apt install -y make

# Copy requirements and install
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app files
COPY . .
COPY .env.local .env.local

# Expose the port Flask runs on
EXPOSE 5173

# Start the Flask app
CMD ["make", "run-dev"]
