#!/bin/bash

# InnerSource Hub - Local Development Startup Script
# This script starts the database in Docker and runs frontend/backend locally

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}Starting InnerSource Hub local development environment...${NC}"
echo ""

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo -e "${RED}Error: Docker is not running. Please start Docker and try again.${NC}"
    exit 1
fi

# Start PostgreSQL database
echo -e "${YELLOW}→ Starting PostgreSQL database in Docker...${NC}"
DB_CONTAINER=$(docker ps -q -f name=innersource_db)

if [ -z "$DB_CONTAINER" ]; then
    # Check if container exists but is stopped
    STOPPED_CONTAINER=$(docker ps -a -q -f name=innersource_db)
    if [ -n "$STOPPED_CONTAINER" ]; then
        docker start innersource_db
    else
        docker run -d \
            --name innersource_db \
            -e POSTGRES_USER=user \
            -e POSTGRES_PASSWORD=password \
            -e POSTGRES_DB=innersourcehub \
            -p 5432:5432 \
            postgres:15
    fi
    echo -e "${GREEN}✓ Database started${NC}"
else
    echo -e "${GREEN}✓ Database already running${NC}"
fi

# Wait for database to be ready
echo -e "${YELLOW}→ Waiting for database to be ready...${NC}"
until docker exec innersource_db pg_isready -U user > /dev/null 2>&1; do
    sleep 1
done
echo -e "${GREEN}✓ Database is ready${NC}"
echo ""

# Start Backend
echo -e "${YELLOW}→ Starting backend (FastAPI)...${NC}"
cd backend

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo -e "${YELLOW}  Creating Python virtual environment...${NC}"
    uv venv || python3 -m venv .venv
fi

# Activate virtual environment and install dependencies
echo -e "${YELLOW}  Installing backend dependencies...${NC}"
uv pip install -q fastapi uvicorn sqlalchemy psycopg2-binary || pip install -q fastapi uvicorn sqlalchemy psycopg2-binary

# Start backend in background
export DATABASE_URL="postgresql://user:password@localhost/innersourcehub"
echo -e "${YELLOW}  Starting uvicorn server on port 8000...${NC}"
uvicorn app.main:app --reload --port 8000 > /tmp/innersource_backend.log 2>&1 &
BACKEND_PID=$!
echo $BACKEND_PID > /tmp/innersource_backend.pid
echo -e "${GREEN}✓ Backend started (PID: $BACKEND_PID)${NC}"

cd ..
echo ""

# Wait for backend to be ready
echo -e "${YELLOW}→ Waiting for backend to be ready...${NC}"
sleep 3
echo -e "${GREEN}✓ Backend is ready${NC}"
echo ""

# Start Frontend
echo -e "${YELLOW}→ Starting frontend (React)...${NC}"
cd frontend

# Install dependencies if node_modules doesn't exist
if [ ! -d "node_modules" ]; then
    echo -e "${YELLOW}  Installing frontend dependencies...${NC}"
    pnpm install || npm install
fi

# Start frontend in background
echo -e "${YELLOW}  Starting React dev server on port 3000...${NC}"
pnpm start > /tmp/innersource_frontend.log 2>&1 &
FRONTEND_PID=$!
echo $FRONTEND_PID > /tmp/innersource_frontend.pid
echo -e "${GREEN}✓ Frontend started (PID: $FRONTEND_PID)${NC}"

cd ..
echo ""

# Display access information
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}✓ InnerSource Hub is running locally!${NC}"
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo -e "  Frontend:         ${YELLOW}http://localhost:3000${NC}"
echo -e "  Backend API:      ${YELLOW}http://localhost:8000${NC}"
echo -e "  API Documentation: ${YELLOW}http://localhost:8000/docs${NC}"
echo ""
echo -e "  Backend log:      ${YELLOW}tail -f /tmp/innersource_backend.log${NC}"
echo -e "  Frontend log:     ${YELLOW}tail -f /tmp/innersource_frontend.log${NC}"
echo ""
echo -e "To stop all services, run: ${YELLOW}./stop-local.sh${NC}"
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
