#!/bin/bash

# InnerSource Hub - Local Development Stop Script
# This script stops the frontend, backend, and database

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}Stopping InnerSource Hub local development environment...${NC}"
echo ""

# Function to kill processes listening on a port
kill_port() {
    local port=$1
    local name=$2
    local pid=$(lsof -ti:$port 2>/dev/null)
    if [ -n "$pid" ]; then
        echo -e "${YELLOW}→ Stopping $name (PID: $pid, Port: $port)...${NC}"
        kill -9 $pid 2>/dev/null
        echo -e "${GREEN}✓ $name stopped${NC}"
        return 0
    fi
    return 1
}

# Stop Frontend (try PID file first, then port 3000)
FRONTEND_STOPPED=0
if [ -f /tmp/innersource_frontend.pid ]; then
    FRONTEND_PID=$(cat /tmp/innersource_frontend.pid)
    if ps -p $FRONTEND_PID > /dev/null 2>&1; then
        echo -e "${YELLOW}→ Stopping frontend (PID: $FRONTEND_PID)...${NC}"
        kill $FRONTEND_PID 2>/dev/null
        echo -e "${GREEN}✓ Frontend stopped${NC}"
        FRONTEND_STOPPED=1
    fi
    rm /tmp/innersource_frontend.pid
fi

if [ $FRONTEND_STOPPED -eq 0 ]; then
    kill_port 3000 "Frontend" || echo -e "${YELLOW}→ Frontend not running${NC}"
fi
echo ""

# Stop Backend (try PID file first, then port 8000)
BACKEND_STOPPED=0
if [ -f /tmp/innersource_backend.pid ]; then
    BACKEND_PID=$(cat /tmp/innersource_backend.pid)
    if ps -p $BACKEND_PID > /dev/null 2>&1; then
        echo -e "${YELLOW}→ Stopping backend (PID: $BACKEND_PID)...${NC}"
        kill $BACKEND_PID 2>/dev/null
        echo -e "${GREEN}✓ Backend stopped${NC}"
        BACKEND_STOPPED=1
    fi
    rm /tmp/innersource_backend.pid
fi

if [ $BACKEND_STOPPED -eq 0 ]; then
    # First try graceful kill on port 8000, then force kill if needed
    BACKEND_PID=$(lsof -ti:8000 2>/dev/null)
    if [ -n "$BACKEND_PID" ]; then
        echo -e "${YELLOW}→ Stopping backend (PID: $BACKEND_PID, Port: 8000)...${NC}"
        kill $BACKEND_PID 2>/dev/null
        sleep 1
        # If still running, force kill
        if ps -p $BACKEND_PID > /dev/null 2>&1; then
            kill -9 $BACKEND_PID 2>/dev/null
        fi
        echo -e "${GREEN}✓ Backend stopped${NC}"
    else
        echo -e "${YELLOW}→ Backend not running${NC}"
    fi
fi
echo ""

# Stop Database
DB_CONTAINER=$(docker ps -q -f name=innersource_db)
if [ -n "$DB_CONTAINER" ]; then
    echo -e "${YELLOW}→ Stopping database container...${NC}"
    docker stop innersource_db
    echo -e "${GREEN}✓ Database stopped${NC}"
else
    echo -e "${YELLOW}→ Database container not running${NC}"
fi
echo ""

echo -e "${GREEN}✓ All services stopped${NC}"
