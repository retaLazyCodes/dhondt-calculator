#!/bin/sh

# Run database migrations
poetry run alembic upgrade head

# Start the FastAPI application
poetry run uvicorn core.server:app --host 0.0.0.0 --port 8000
