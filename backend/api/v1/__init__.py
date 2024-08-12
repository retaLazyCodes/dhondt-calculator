from fastapi import APIRouter

from .monitoring import monitoring_router
from .elections import election_router

v1_router = APIRouter()
v1_router.include_router(monitoring_router, prefix="/monitoring")
v1_router.include_router(election_router, prefix="/elections")