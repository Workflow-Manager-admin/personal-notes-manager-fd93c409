from sqlalchemy.orm import Session
from . import models, schemas

# PUBLIC_INTERFACE
def get_note(db: Session, note_id: int):
    """Get a note by its ID."""
    return db.query(models.Note).filter(models.Note.id == note_id).first()

# PUBLIC_INTERFACE
def get_notes(db: Session, skip: int = 0, limit: int = 100):
    """Return a paginated list of notes."""
    return db.query(models.Note).offset(skip).limit(limit).all()

# PUBLIC_INTERFACE
def create_note(db: Session, note: schemas.NoteCreate):
    """Create a new note."""
    db_note = models.Note(title=note.title, content=note.content)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

# PUBLIC_INTERFACE
def update_note(db: Session, note_id: int, note: schemas.NoteUpdate):
    """Update an existing note by its ID."""
    db_note = get_note(db, note_id)
    if not db_note:
        return None
    if note.title is not None:
        db_note.title = note.title
    if note.content is not None:
        db_note.content = note.content
    db.commit()
    db.refresh(db_note)
    return db_note

# PUBLIC_INTERFACE
def delete_note(db: Session, note_id: int):
    """Delete a note by its ID."""
    db_note = get_note(db, note_id)
    if not db_note:
        return None
    db.delete(db_note)
    db.commit()
    return db_note
