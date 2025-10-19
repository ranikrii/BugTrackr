# Bug Tracker API

A lightweight **FastAPI-based Bug Tracking System** that allows users to create, read, update, and delete (CRUD) bug reports efficiently.  
Built with **Python, FastAPI, SQLAlchemy**, and **PostgreSQL** — designed for scalability and easy deployment on **Render**.

---

## Features

- **Bug Management** — Create, list, update, and delete bug reports.  
- **User Authentication** — Secure JWT-based login system.  
- **PostgreSQL Database** — Managed via SQLAlchemy ORM.  
- **FastAPI Docs** — Interactive Swagger UI (`/docs`) and Redoc (`/redoc`).  
- **Optional Sentry Integration** — Error monitoring for production.  
- **Docker Support** — Ready-to-deploy with Docker or Docker Compose.


## Setup
create virtual environment and install dependencies (pip install -r requirements.txt).
Create .env file following [.env]

## Run the app and visit
uvicorn app.main:app --reload
http://127.0.0.1:8000/docs

## Tech Stack
FastAPI — Modern async Python web framework
PostgreSQL — Relational database
SQLAlchemy — ORM
Pydantic — Data validation
Sentry — Error monitoring (optional)
Render — Cloud deployment platform
Docker — Containerized deployment