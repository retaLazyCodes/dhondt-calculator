from pydantic import BaseModel, field_validator, conlist
from typing import List

class ElectionRequest(BaseModel):
    seats: int
    votes: List[int]

    @field_validator('seats')
    def check_seats_positive(cls, value):
        if value <= 0:
            raise ValueError('Seats must be a positive integer')
        return value

    @field_validator('votes')
    def check_votes_non_negative(cls, value):
        if any(vote < 0 for vote in value):
            raise ValueError('Votes must be non-negative integers')
        return value

class ElectionResult(BaseModel):
    results: List[int]

class ElectionResponse(ElectionRequest, ElectionResult):
    id: int