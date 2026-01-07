# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

InnerSource Hub is a Proof-of-Concept (PoC) enterprise platform for increasing project visibility and cross-team collaboration. It centralizes internal projects through an AI-enhanced portal that tracks projects from "Idea" through "Scale" phases.

## Quick Start Commands

```bash
# Local development (database in Docker, frontend/backend locally)
./start-local.sh

# Stop all services
./stop-local.sh

# Full Docker setup
docker-compose up --build

# Backend only (requires database running)
cd backend
DATABASE_URL="postgresql://user:password@localhost/innersourcehub" uvicorn app.main:app --reload --port 8000

# Frontend only
cd frontend
pnpm install && pnpm start

# Install backend dependencies
cd backend
uv pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic requests

# Install frontend dependencies
cd frontend
pnpm install
```

## Access Points

- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Documentation (Swagger UI): http://localhost:8000/docs

## Architecture

### Stack

```
Frontend (React) ←→ Backend (FastAPI) ←→ Database (PostgreSQL)
                                    ↓
                              Mock RAGFlow (AI Search)
```

### Backend Structure (`backend/app/`)

- **main.py**: FastAPI application with REST endpoints
- **models.py**: SQLAlchemy ORM models (User, Project, Engagement)
- **schemas.py**: Pydantic request/response schemas
- **database.py**: SQLAlchemy engine and session management
- **ragflow_mock.py**: Mock RAGFlow integration for AI search
- **seeder.py**: Automatic database seeding on startup

Key patterns:
- FastAPI dependency injection for database sessions (`Depends(get_db)`)
- Enum-based status system: `ProjectStatus.IDEA → POC → BUILD → SCALE`
- Automatic database seeding via `@app.on_event("startup")`
- CORS enabled for all origins (PoC simplification)

### Frontend Structure (`frontend/src/`)

- **App.js**: React Router setup with routes for `/`, `/submit`, `/search`
- **api.js**: Axios instance configured with `baseURL: 'http://localhost:8000'`
- **components/**:
  - `ProjectDashboard.js`: Card-based project view with status filtering
  - `ProjectSubmissionForm.js`: New project creation form
  - `SearchInterface.js`: Natural language search UI
  - `Navbar.js`: Navigation between sections

Key patterns:
- Functional components with hooks
- Local state management (useState)
- Direct API calls via axios

### Database Models

**User**: email, department, skills (comma-separated), avatar_url
**Project**: name, description, problem_statement, status (enum), vcs_url, owner_id, tags (comma-separated), help_wanted_roles (comma-separated)
**Engagement**: type (Upvote/Comment/Follow), user_id, project_id, content

Relationships:
- User → Projects (owner)
- User → Engagements
- Project → Owner (User)
- Project → Engagements

### API Endpoints

- `POST /users/` - Create user
- `GET /users/` - List users
- `GET /users/{id}` - Get user
- `POST /projects/` - Create project
- `GET /projects/` - List projects
- `GET /projects/{id}` - Get project with engagements
- `PUT /projects/{id}` - Update project
- `POST /projects/{id}/ingest` - Simulate VCS ingestion
- `POST /engagements/` - Create engagement (upvote/comment/follow)
- `GET /search/?query=...` - Natural language search via RAGFlow mock

### RAGFlow Mock Integration

The mock RAGFlow (`ragflow_mock.py`) simulates:
- Document ingestion from VCS URLs
- Keyword-based natural language search
- Relevance scoring with match reasons

In production, replace `ragflow_mock` with actual RAGFlow API calls.

### Database Connection

Local development: `DATABASE_URL="postgresql://user:password@localhost/innersourcehub"`
Docker: `DATABASE_URL="postgresql://user:password@db/innersourcehub"`

The backend automatically falls back to the Docker host (`db`) when `DATABASE_URL` is not set.

### Data Seeding

The backend automatically seeds sample data on startup via `seeder.seed_db()`. This includes:
- Sample users with different departments and skills
- Example projects at various lifecycle stages
- Sample engagements (upvotes, follows)

## Python Environment

The project uses Python 3.12+. Use `uv` for faster package management:

```bash
uv python pin 3.12
uv pip install -r backend/requirements.txt
```

## Frontend Package Manager

The project uses `pnpm` by default. 

```bash
pnpm install  # preferred
pnpm start    # preferred
```

## Project Status Workflow

Projects progress through these stages:
1. **Idea**: Initial concept submission
2. **PoC**: Proof of concept in progress
3. **Build**: Actively being developed
4. **Scale**: Mature and widely adopted

The frontend dashboard displays projects grouped by status, and projects can be updated via PUT `/projects/{id}`.
