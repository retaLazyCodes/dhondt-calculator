from fastapi import FastAPI, HTTPException, Request
from typing import List

app = FastAPI(
    title="FastAPI D'Hondt Seat Allocation",
    description="API para calcular la distribución de escaños utilizando el sistema D'Hondt.",
    version="0.0.1",
    contact={
        "name": "Brian",
        "email": "brianretamar0101@gmail.com",
    },
    license_info={
        "name": "MIT",
    },
)


@app.get("/healthcheck")
def healthcheck():
    return {"status": "healthy"}


@app.post("/calculate_seats")
async def calculate_seats(request: Request):
    try:
        data = await request.json()
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid given data")
    
    if 'seats' not in data or 'votes' not in data:
        raise HTTPException(status_code=400, detail="Missing 'seats' or 'votes' in request body")
    
    seats = data['seats']
    votes = data['votes']

    if not isinstance(seats, int) or seats <= 0:
        raise HTTPException(status_code=400, detail="'seats' must be a positive integer")
    if not isinstance(votes, list) or not votes:
        raise HTTPException(status_code=400, detail="'votes' must be a non-empty list of integers")
    if not all(isinstance(v, int) and v >= 0 for v in votes):
        raise HTTPException(status_code=400, detail="All elements in 'votes' must be non-negative integers")

    results = calculate_dhondt(seats, votes)
    return {"results": results}

def calculate_dhondt(seats: int, votes: List[int]) -> List[int]:
    allocation = [0] * len(votes)
    for _ in range(seats):
        quotients = [votes[i] / (allocation[i] + 1) for i in range(len(votes))]
        winner = quotients.index(max(quotients))
        allocation[winner] += 1
    return allocation