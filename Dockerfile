# Use Python 3.9 slim base image for a lightweight starting point
FROM python:3.9-slim AS builder

WORKDIR /code

# Copy the entire application code into the container's working directory
COPY . /code

# Use --no-cache-dir to avoid caching downloaded packages, reducing image size
RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]