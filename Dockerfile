# Use a lightweight Python image
FROM python:3.10-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget unzip curl xvfb \
    && apt-get clean

# Install pip and required Python libraries
RUN pip install --upgrade pip

# Copy your project files
WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

# Run your script
CMD ["python", "reschedule.py"]
