from pydantic import BaseModel
from typing import List

class ElectionRequest(BaseModel):
    seats: int
    votes: List[int]

class ElectionResult(BaseModel):
    results: List[int]
