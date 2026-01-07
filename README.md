# InnerSource Hub (PoC)

## Product Objective
To validate that a centralized, AI-enhanced portal can increase project visibility and cross-team collaboration within the enterprise by providing a single source of truth for the "Idea" through "Scale" phases.

## Scope & Features

### 1. Idea & Project Management Module (The "State Machine")
- **Submission Portal**: Form to capture Project Name, Description, Problem Statement, Current Phase, Tech Stack, VCS URL.
- **Project Dashboard**: Card View showing projects moving through phases (Idea, PoC, Build, Scale).
- **Collaboration Flare**: Toggle for "Help Wanted" with specific roles.

### 2. AI Discovery Module (The RAGFlow Integration)
- **Natural Language Search**: "Chat with your Codebase" interface.
- **Contextual Results**: Mocked RAGFlow integration returns relevant projects with summaries.

### 3. Social & Recognition (The "Culture" Layer)
- **Upvoting/Following**: (Data model support included, UI simplified for PoC).
- **Contributor Profiles**: (Data model support included).

## Technical Architecture

### Architecture Diagram

```mermaid
graph TD
    User[User] --> Frontend[Frontend (React + Nginx)]
    Frontend --> Backend[Backend (FastAPI)]
    Backend --> DB[(PostgreSQL)]
    Backend --> RAGFlow[RAGFlow Mock (Intelligence)]

    subgraph "InnerSource Hub"
        Frontend
        Backend
        DB
        RAGFlow
    end
```

### Components
- **Frontend**: React (SPA) hosted on Nginx.
- **Backend**: FastAPI (Python) handling CRUD and acting as a wrapper for RAGFlow.
- **Database**: PostgreSQL (Single instance).
- **Intelligence**: Mocked RAGFlow service for document ingestion and search.

## Setup & Running

### Prerequisites
- Docker and Docker Compose

### Steps
1. Clone the repository.
2. Run `docker-compose up --build`.
3. Access the Frontend at `http://localhost:3000`.
4. Access the Backend API Docs at `http://localhost:8000/docs`.

### Sample Data Creation
Once the system is running, you can use the Swagger UI (`http://localhost:8000/docs`) or the Frontend "Submit Idea" form to create data.

Example Projects to add:
1. **Centralized Logging Wrapper**
   - Problem: Every team writes their own logging config.
   - Stack: Java, Python
   - Status: Idea
2. **Kafka Monitoring Tool**
   - Problem: No visibility into consumer lag.
   - Stack: Go, React
   - Status: PoC
   - VCS URL: https://github.com/example/kafka-monitor

## Directory Structure
- `backend/`: FastAPI application code.
- `frontend/`: React application code.
- `docker-compose.yml`: Container orchestration configuration.
