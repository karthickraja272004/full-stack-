# Python Docker API

## Project Overview

This project is a simple REST API built using Flask and containerized using Docker.

It demonstrates:

- Flask REST API
- Docker containerization
- Logging
- Exception handling
- Docker image creation
- Running applications inside containers

---

## Project Structure

```
python-docker-api/
│
├── app1.py
├── Dockerfile
├── requirements.txt
├── logs/
│   └── app1.log
└── README.md
```

---

## Requirements

- Python 3.14
- Docker Desktop

---

## Local Execution

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app1.py
```

Open:

```
http://localhost:5000
```

---

## Docker Build

```bash
docker build -t python-demo:v1 .
```

---

## Run Docker Container

```bash
docker run -p 5000:5000 --name python-container python-demo:v1
```

---

## API Endpoints

### Home

```
GET /
```

### Users

```
GET /users/<user_id>
```

Example:

```
GET /users/1
```

---

### Organization

```
GET /organization
```

---

### Status

```
GET /status
```

---

## Features

- Flask REST API
- JSON Responses
- Input Validation
- Error Handling
- Logging
- Dockerized Application

---

## Author

Karthick Raja