# Python build
FROM python:3.8-slim

# get tree util
RUN apt-get update && apt-get install tree

# copy repo root to app directory
COPY . / /app/

# Set working directory
WORKDIR /app/

# Install requirements
RUN pip install -r requirements.txt

# Expose port 8050
EXPOSE 8050
ENV LISTEN_PORT=8050

# Run python test script
ENTRYPOINT ["python"]
CMD ["main.py"]
