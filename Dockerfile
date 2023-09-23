#Importing the official OS image (ubuntu) frm docker repository
FROM ubuntu:20.04

# Install system dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip


# Copy application code and dependencies to the container
COPY ./* /app

#Setting working directory inside container
WORKDIR /app


# Install Python dependencies
RUN pip3 install -r requirements.txt

# Expose the port your application will run on
EXPOSE 8000

# Command to run your application
CMD ["python3", "app.py"]
