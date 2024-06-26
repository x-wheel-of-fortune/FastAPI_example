import datetime
from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    """Base model for user data."""
    login: str
    password: str
    project_id: str
    env: str
    domain: str


class UserCreate(UserBase):
    """Model for creating a new user."""
    pass


class User(UserBase):
    """Model for user ID, creation timestamp, and lock timestamp."""
    id: str
    created_at: Optional[datetime.datetime]
    locktime: Optional[datetime.datetime]

    class Config:
        """Pydantic configuration."""
        from_attributes = True
