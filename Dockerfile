FROM python:3.11.6-slim-bullseye

# Set environment variables
ARG AZURE_KEY
ARG AZURE_REGION
ARG PORT
ARG HOST='0.0.0.0'

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# build .env file
RUN touch .env
RUN echo "AZURE_KEY=$AZURE_KEY" >> .env
RUN echo "AZURE_REGION=$AZURE_REGION" >> .env
RUN echo "HOST=$HOST" >> .env
RUN echo "PORT=$PORT" >> .env

# Install any needed packages specified in requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install --upgrade accelerate

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run app.py when the container launches
CMD ["gunicorn", "app:app"]