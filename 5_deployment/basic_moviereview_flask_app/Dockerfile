# Use this for deploying app in custom runtime environment

FROM python:3.7

# Create working directory
WORKDIR /app

# Copy requirements.txt file
COPY requirements.txt ./requirements.txt

# Install dependencies
RUN pip3 install -r requirements.txt

# Expose port
EXPOSE 8080

# Copy all files for app
COPY . /app

#Run app
CMD ["gunicorn", "app:app", "-b", ":8080", "--timeout", "300"]
