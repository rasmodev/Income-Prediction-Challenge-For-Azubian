# Use the official Python image as a parent image
FROM python:3.11.3-slim

# Set the working directory within the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY ./requirements.txt /app/requirements.txt

# Install the Python dependencies
RUN pip install -r /app/requirements.txt

# Copy your Streamlit application code into the container
COPY ./app.py /app/app.py

# Copy the model and key components into the container
COPY ./model_and_key_components.pkl /app/model_and_key_components.pkl

# Expose port 8000 for the FastAPI application
EXPOSE 7860

# Command to start the Streamlit app
CMD ["streamlit", "run", "--server.port", "7860", "app.py"]