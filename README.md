# MovieDBREST

## Overview
MovieDBREST is a Single Page Application (SPA) featuring a RESTful backend implemented using FastAPI and a dynamic frontend built with React. This project demonstrates the creation of a database-driven API with endpoints for managing movies and actors.

---

## Requirements

### Backend:
- Python 3.8+
- FastAPI
- Peewee (ORM for database management)
- SQLite (default database)

### Frontend:
- ReactJS (for dynamic client-side rendering)

---

## Setup Instructions

### 1. Install Dependencies
Ensure you have Python installed, then install the required Python libraries:
```bash
pip install "fastapi[standard]"
pip install peewee
```

### 2. Project Structure
The project is divided into multiple files:

- **database.py**: Initializes the database and manages connections.
- **models.py**: Defines database models using Peewee.
- **schemas.py**: Defines Pydantic models for data validation and serialization.
- **main.py**: Contains the FastAPI application and endpoint definitions.

### 3. Run the Application
To start the FastAPI application:

```bash
uvicorn main:app --reload
```

Access the interactive API documentation at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## API Endpoints

### Movies Endpoints
- **GET** `/movies`: Retrieve a list of all movies.
- **GET** `/movies/{movie_id}`: Retrieve details of a specific movie by ID.
- **POST** `/movies`: Add a new movie.
  - Example request body:
    ```json
    {
      "title": "Inception",
      "year": 2010,
      "director": "Christopher Nolan",
      "description": "A mind-bending thriller."
    }
    ```
- **DELETE** `/movies/{movie_id}`: Delete a specific movie by ID.

### Actors Endpoints
- **GET** `/actors`: Retrieve a list of all actors.
- **GET** `/actors/{actor_id}`: Retrieve details of a specific actor by ID.
- **POST** `/actors`: Add a new actor.
  - Example request body:
    ```json
    {
      "name": "Leonardo",
      "surname": "DiCaprio"
    }
    ```
- **POST** `/movies/{movie_id}/actors`: Add an existing actor to a movie.

---

## Database Configuration

The project uses SQLite as the default database. The database file is named `movies.db`.

To create tables and initialize the database, run the following script:

```python
from models import db, Actor, Movie, ActorMovie

db.connect()
db.create_tables([Actor, Movie, ActorMovie])
db.close()
```

---

## Testing the API

### Using HTTP Client
You can test the API using the provided `test_main.http` file or tools like [Postman](https://www.postman.com/) or [cURL](https://curl.se/).

### Example cURL Requests

1. **Get all movies:**
    ```bash
    curl -X GET http://127.0.0.1:8000/movies
    ```

2. **Add a new movie:**
    ```bash
    curl -X POST http://127.0.0.1:8000/movies \
    -H "Content-Type: application/json" \
    -d '{
        "title": "Inception",
        "year": 2010,
        "director": "Christopher Nolan",
        "description": "A mind-bending thriller."
    }'
    ```



