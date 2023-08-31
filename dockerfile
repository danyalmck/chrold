# Use the mlflow base image
FROM ghcr.io/mlflow/mlflow

ARG DB_HOST
ARG DB_USERNAME
ARG DB_PASS

ENV DATABRICKS_HOST=${DB_HOST}
ENV DATABRICKS_USERNAME=${DB_USERNAME}
ENV DATABRICKS_PASSWORD=${DB_PASS}


# Install useful tools
RUN apt-get update && \
    apt-get install -y \
    wget \
    curl \
    unzip \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set a working directory
WORKDIR /app

# Copy your code to the filesystem
COPY . /app

# Execute the train.py script
CMD ["python", "/app/main.py"]
