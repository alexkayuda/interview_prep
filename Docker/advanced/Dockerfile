# Dockerfile

# Stage 1: Build Stage
FROM python:3.9-slim AS build

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Stage 2: Final Stage
FROM python:3.9-slim

# Copy installed dependencies from the build stage
COPY --from=build /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=build /usr/local/bin /usr/local/bin

# Copy the application code from the build stage
COPY --from=build /app /app

# Set the working directory
WORKDIR /app

# Expose the Flask port
EXPOSE 5000

# Define the entrypoint
CMD ["flask", "run", "--host=0.0.0.0"]
