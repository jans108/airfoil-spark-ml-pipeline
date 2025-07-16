FROM python:3.12

# Install Java (required for PySpark)
RUN apt-get update && \
    apt-get install -y --no-install-recommends openjdk-17-jre-headless && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set Java environment variables
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

# Set the working directory
WORKDIR /app

# Healthcheck to ensure Spark is running
# HEALTHCHECK --interval=30s --timeout=15s --start-period=90s --retries=3 \
#    CMD python -c "import findspark; findspark.init(); import pyspark; print('Spark OK')" || exit 1

# Copy the requirements file into the container
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

CMD [ "python", "main.py" ]