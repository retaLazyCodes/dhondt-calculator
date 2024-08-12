from fastapi import APIRouter

from .elections import election_router

elections_router = APIRouter()
elections_router.include_router(election_router, prefix="/elections", tags=["elections"])

__all__ = ["election_router"]