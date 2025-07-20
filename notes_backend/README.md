# Notes Backend – FastAPI

This backend provides a REST API for CRUD (Create, Read, Update, Delete) operations on personal notes.

## Features

- **Create** a new note
- **List** (read) all notes
- **Get** a note by its ID
- **Update** a note
- **Delete** a note

## Tech Stack

- Python 3.10+
- FastAPI
- SQLAlchemy + SQLite (default, can override using `NOTES_DB_URL` env var)
- Pydantic

## Project Structure

```
src/api/
    main.py         # FastAPI application and endpoints
    models.py       # SQLAlchemy models
    schemas.py      # Pydantic schemas
    crud.py         # CRUD database functions
    database.py     # DB connection/session setup
```

## Running Locally

1. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. (Optional) Configure the database (defaults to SQLite file `notes.db`).
    - To use a different DB, set `NOTES_DB_URL` in the environment.

3. Start the FastAPI server:

    ```bash
    uvicorn src.api.main:app --reload
    ```

4. API Docs available at [http://localhost:8000/docs](http://localhost:8000/docs)

## Environment Variables

- `NOTES_DB_URL`: Database URL (optional, defaults to `sqlite:///./notes.db`)

## API Endpoints

| METHOD | PATH           | DESCRIPTION         |
|--------|----------------|--------------------|
| GET    | `/`            | Health check       |
| POST   | `/notes/`      | Create note        |
| GET    | `/notes/`      | List notes         |
| GET    | `/notes/{id}`  | Get note by ID     |
| PUT    | `/notes/{id}`  | Update note        |
| DELETE | `/notes/{id}`  | Delete note        |

All endpoints return JSON.

## License

MIT License
