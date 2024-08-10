import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        app="core.server:app",
        reload=True,
        workers=1,
    )


# @app.post("/calculate_seats/", response_model=ElectionResult)
# async def calculate_seats(election_request: ElectionRequest):
#     seats = election_request.seats
#     votes = election_request.votes
    
#     if seats <= 0:
#         raise HTTPException(status_code=400, detail="Number of seats must be greater than zero")
#     if not votes:
#         raise HTTPException(status_code=400, detail="Votes cannot be empty")
#     if not all(isinstance(v, int) and v >= 0 for v in votes):
#         raise HTTPException(status_code=400, detail="All elements in 'votes' must be non-negative integers")

#     results = calculate_dhondt(seats, votes)
#     return ElectionResult(results=results)

# def calculate_dhondt(seats: int, votes: List[int]) -> List[int]:
#     allocation = [0] * len(votes)
#     for _ in range(seats):
#         quotients = [votes[i] / (allocation[i] + 1) for i in range(len(votes))]
#         winner = quotients.index(max(quotients))
#         allocation[winner] += 1
#     return allocation