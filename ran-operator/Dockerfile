FROM python:3.7-alpine

# Install system dependencies
RUN apk --no-cache add gcc musl-dev curl bash

# Set up a non-root user
RUN addgroup -S worker && adduser -D -h /home/worker -s /bin/bash worker -G worker
USER worker
WORKDIR /home/worker

# Copy requirements.txt separately to leverage Docker caching
COPY --chown=worker:worker /app/requirements.txt requirements.txt
RUN pip install --upgrade pip \
    && pip install cython \
    && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY --chown=worker:worker /app /home/worker/app

# Set the PATH environment variable
ENV PATH="/home/worker/.local/bin:${PATH}"

# Make the operator script executable
RUN chmod +x /home/worker/app/operator.bash

# Set the entrypoint
ENTRYPOINT ["/bin/bash", "-c", "/home/worker/app/operator.bash"]

