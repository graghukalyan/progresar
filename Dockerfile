# Use an image supported by Amazon ECR
FROM public.ecr.aws/docker/library/python:alpine3.19

RUN apk update && apk add --no-cache python3 && rm -rf /var/cache/apk/*

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --ignore-installed -r requirements.txt

# Install Poetry
RUN pip install poetry

# Install project dependencies
RUN poetry install

# Install Nginx
RUN apk update && apk add --no-cache nginx

# Copy Nginx configuration file
COPY nginx.conf /etc/nginx/nginx.conf

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["sh", "-c", "nginx && poetry run python app/main.py"]
