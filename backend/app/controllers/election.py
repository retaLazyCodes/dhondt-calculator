from app.models import Election
from app.schemas import ElectionResponse
from app.repositories import ElectionRepository
from core.controller import BaseController


class ElectionController(BaseController[Election]):
    """Election controller."""

    def __init__(self, election_repository: ElectionRepository):
        super().__init__(model=Election, repository=election_repository)
        self.election_repository = election_repository

    def register_calculation(self, seats: int, votes: list[int]) -> ElectionResponse:
        """
        Performs the calculation of seat distribution using the D'Hondt system and creates the model instance.
        """
        results = [0] * len(votes)
        for _ in range(seats):
            quotients = [votes[i] / (results[i] + 1) for i in range(len(votes))]
            winner = quotients.index(max(quotients))
            results[winner] += 1

        return self.election_repository.create(
            {
                "seats": seats,
                "votes": votes,
                "results": results
            }
        )