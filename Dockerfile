# # Dockerfile

# # Use official Python base image
# FROM python:3.10-slim

# # Set environment vars
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1

# # Set work directory
# WORKDIR /code

# # Install dependencies
# COPY requirements.txt /code/
# RUN pip install --upgrade pip && pip install -r requirements.txt

# # Copy project files
# COPY . /code/

# # Expose port
# EXPOSE 8000

# # Run the app
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


# Dockerfile

FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /code/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
