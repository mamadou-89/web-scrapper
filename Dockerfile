# Dockerfile for a Flask web application that scrapes web pages
FROM python:3.13.5-slim
LABEL maintainer="mamad"
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8080"]

# Expose port 8080 for the Flask application
EXPOSE 8080