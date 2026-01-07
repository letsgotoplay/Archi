# Database Models for InnerSource Hub PoC
# Defines the schema for Projects, Users, and Engagement.

from sqlalchemy import Column, Integer, String, Enum, ForeignKey, Text, DateTime, ARRAY
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum
from .database import Base

class ProjectStatus(str, enum.Enum):
    IDEA = "Idea"
    POC = "PoC"
    BUILD = "Build"
    SCALE = "Scale"

class EngagementType(str, enum.Enum):
    UPVOTE = "Upvote"
    COMMENT = "Comment"
    FOLLOW = "Follow"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    department = Column(String)
    skills = Column(String) # Stored as comma-separated string for simplicity in PoC
    avatar_url = Column(String, nullable=True)

    projects = relationship("Project", back_populates="owner")
    engagements = relationship("Engagement", back_populates="user")

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)
    problem_statement = Column(Text)
    status = Column(Enum(ProjectStatus), default=ProjectStatus.IDEA)
    vcs_url = Column(String, nullable=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    tags = Column(String) # Comma-separated
    help_wanted_roles = Column(String, nullable=True) # Comma-separated

    owner = relationship("User", back_populates="projects")
    engagements = relationship("Engagement", back_populates="project")

class Engagement(Base):
    __tablename__ = "engagements"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    project_id = Column(Integer, ForeignKey("projects.id"))
    type = Column(Enum(EngagementType))
    content = Column(Text, nullable=True) # For comments
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="engagements")
    project = relationship("Project", back_populates="engagements")
