# Pydantic Schemas for InnerSource Hub PoC
# Defines the request and response models for the API.

from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from .models import ProjectStatus, EngagementType

class UserBase(BaseModel):
    email: str
    department: Optional[str] = None
    skills: Optional[str] = None
    avatar_url: Optional[str] = None

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        from_attributes = True

class EngagementBase(BaseModel):
    type: EngagementType
    content: Optional[str] = None

class EngagementCreate(EngagementBase):
    user_id: int
    project_id: int

class Engagement(EngagementBase):
    id: int
    user_id: int
    project_id: int
    created_at: datetime

    class Config:
        from_attributes = True

class ProjectBase(BaseModel):
    name: str
    description: str
    problem_statement: str
    status: ProjectStatus = ProjectStatus.IDEA
    vcs_url: Optional[str] = None
    tags: Optional[str] = None
    help_wanted_roles: Optional[str] = None

class ProjectCreate(ProjectBase):
    owner_id: int

class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    problem_statement: Optional[str] = None
    status: Optional[ProjectStatus] = None
    vcs_url: Optional[str] = None
    tags: Optional[str] = None
    help_wanted_roles: Optional[str] = None

class Project(ProjectBase):
    id: int
    owner_id: int
    created_at: datetime
    owner: Optional[User] = None

    class Config:
        from_attributes = True

class ProjectWithEngagements(Project):
    engagements: List[Engagement] = []

    class Config:
        from_attributes = True
