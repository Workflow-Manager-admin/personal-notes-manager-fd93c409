from pydantic import BaseModel, Field

# PUBLIC_INTERFACE
class NoteBase(BaseModel):
    """Base schema for a note."""
    title: str = Field(..., description="Title of the note")
    content: str = Field(..., description="Content/body of the note")

# PUBLIC_INTERFACE
class NoteCreate(NoteBase):
    """Schema for creating a new note."""
    pass

# PUBLIC_INTERFACE
class NoteUpdate(BaseModel):
    """Schema for updating an existing note."""
    title: str | None = Field(None, description="Title of the note")
    content: str | None = Field(None, description="Content/body of the note")

# PUBLIC_INTERFACE
class Note(NoteBase):
    """Schema for reading a note (with id)."""
    id: int

    class Config:
        from_attributes = True
