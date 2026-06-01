# Personalized News Aggregator API

## Overview

Personalized News Aggregator API is a RESTful backend application built using FastAPI, SQLite, JWT Authentication, and GNews API integration. The application allows users to register, log in securely, save their preferred news categories, and retrieve personalized news articles based on their interests.

This project demonstrates authentication, authorization, database management, external API integration, error handling, and REST API development.

---

## Features

### User Authentication

* User Registration
* User Login
* Password Hashing using bcrypt
* JWT Token Generation and Validation
* Protected Endpoints

### User Preferences

* Save preferred news categories
* Retrieve personalized news feed based on preferences

### News Aggregation

* Search news by keyword
* Fetch personalized news using saved preferences
* Integration with GNews API

### Database

* SQLite Database
* SQLAlchemy ORM
* Persistent User Data
* Persistent Preference Data

### API Documentation

* Interactive Swagger UI
* OpenAPI Documentation

---

## Technology Stack

### Backend

* Python 3.x
* FastAPI

### Database

* SQLite
* SQLAlchemy

### Authentication

* JWT (JSON Web Token)
* Passlib (bcrypt)

### External API

* GNews API

### Testing

* Pytest

---

## Project Structure

```text
news-aggregator-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── auth.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── news.py
│
├── tests/
│   └── test_api.py
│
├── requirements.txt
├── README.md
├── .env
├── .gitignore
└── news.db
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd news-aggregator-api
```

### Create Virtual Environment

Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux/Mac

```bash
python -m venv .venv
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
GNEWS_API_KEY=YOUR_GNEWS_API_KEY
SECRET_KEY=anwar_news_aggregator_super_secret_key_2026
```

---

## Running the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Application URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

OpenAPI Specification:

```text
http://127.0.0.1:8000/openapi.json
```

---

## Database Schema

### Users Table

| Column   | Type    |
| -------- | ------- |
| id       | Integer |
| username | String  |
| email    | String  |
| password | String  |

### Preferences Table

| Column   | Type    |
| -------- | ------- |
| id       | Integer |
| category | String  |
| user_id  | Integer |

---

## API Endpoints

### Root Endpoint

#### GET /

Response

```json
{
  "project": "Personalized News Aggregator API",
  "status": "running"
}
```

---

### User Registration

#### POST /register

Request

```json
{
  "username": "anwar",
  "email": "anwar@example.com",
  "password": "Password123"
}
```

Response

```json
{
  "message": "User registered"
}
```

---

### User Login

#### POST /login

Request

```json
{
  "email": "anwar@example.com",
  "password": "Password123"
}
```

Response

```json
{
  "access_token": "<jwt-token>"
}
```

---

### Save Preferences

#### PUT /preferences

Headers

```text
Authorization: Bearer <jwt-token>
```

Request

```json
{
  "categories": [
    "technology",
    "sports"
  ]
}
```

Response

```json
{
  "message": "Preferences saved"
}
```

---

### Get Personalized News

#### GET /news

Headers

```text
Authorization: Bearer <jwt-token>
```

Response

```json
[
  {
    "title": "Sample News",
    "description": "News Description"
  }
]
```

---

### Search News

#### GET /news/search?q=technology

Response

```json
[
  {
    "title": "Technology News",
    "description": "News Description"
  }
]
```

---

## Authentication Flow

1. Register a new user.
2. Login using registered credentials.
3. Receive JWT token.
4. Authorize using the JWT token.
5. Access protected endpoints.
6. Save preferences and retrieve personalized news.

---

## Testing

Run all test cases:

```bash
pytest
```

Expected Output

```text
====================
3 passed
====================
```

---

## Error Handling

### Invalid Credentials

```json
{
  "detail": "Invalid credentials"
}
```

### Invalid Token

```json
{
  "detail": "Invalid token"
}
```

### Duplicate Email

```json
{
  "detail": "Email already exists"
}
```

---

## Security Features

* Password Hashing using bcrypt
* JWT Authentication
* Protected Routes
* Token Validation
* Input Validation using Pydantic

---

## Future Improvements

* Refresh Tokens
* News Caching
* User Profile Management
* Category Recommendations
* Pagination
* Rate Limiting
* Docker Support
* PostgreSQL Integration

---

## Author

**Anwar Shaik**

Backend System for Personalized News Aggregator API

Built using FastAPI, SQLite, JWT Authentication, and GNews API.
