from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from . import schemas, crud
from .database import engine, SessionLocal, Base

# Initialize models (create tables)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Personal Notes API",
    description="API for managing personal notes. Allows creating, reading, updating, deleting notes.",
    version="1.0.0",
    openapi_tags=[
        {"name": "notes", "description": "Operations on notes"}
    ]
)

# CORS middleware (allowed for demo, restrict in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# PUBLIC_INTERFACE
@app.get("/", tags=["Health"])
def health_check():
    """Health check endpoint."""
    return {"message": "Healthy"}

# PUBLIC_INTERFACE
@app.post("/notes/", response_model=schemas.Note, status_code=status.HTTP_201_CREATED, tags=["notes"], summary="Create a note")
def create_note(note: schemas.NoteCreate, db: Session = Depends(get_db)):
    """
    Create a new personal note.

    - **title**: Title of the note
    - **content**: Content/body of the note
    """
    return crud.create_note(db, note)

# PUBLIC_INTERFACE
@app.get("/notes/", response_model=list[schemas.Note], tags=["notes"], summary="List all notes")
def list_notes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    List notes with pagination.
    """
    return crud.get_notes(db, skip=skip, limit=limit)

# PUBLIC_INTERFACE
@app.get("/notes/{note_id}", response_model=schemas.Note, tags=["notes"], summary="Get a note by ID")
def get_note(note_id: int, db: Session = Depends(get_db)):
    """
    Get a single note by its ID.

    - **note_id**: Unique integer ID of the note
    """
    db_note = crud.get_note(db, note_id)
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return db_note

# PUBLIC_INTERFACE
@app.put("/notes/{note_id}", response_model=schemas.Note, tags=["notes"], summary="Update a note")
def update_note(note_id: int, note: schemas.NoteUpdate, db: Session = Depends(get_db)):
    """
    Update a note by its ID.

    - **note_id**: Unique integer ID of the note
    - **title/content**: New values
    """
    db_note = crud.update_note(db, note_id, note)
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return db_note

# PUBLIC_INTERFACE
@app.delete("/notes/{note_id}", response_model=schemas.Note, tags=["notes"], summary="Delete a note")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    """
    Delete a note by its ID.

    - **note_id**: Unique integer ID of the note
    """
    db_note = crud.delete_note(db, note_id)
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return db_note
