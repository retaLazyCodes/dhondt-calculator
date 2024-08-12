from functools import partial
from fastapi import Depends

from app.controllers import ElectionController
from app.models import Election
from app.repositories import ElectionRepository
from core.database import get_db


class Factory:
    """
    This is the factory container that will instantiate all the controllers and
    repositories which can be accessed by the rest of the application.
    """

    # Repositories
    election_repository = partial(ElectionRepository, Election)

    def get_election_controller(self, db=Depends(get_db)):
        db = next(get_db())
        return ElectionController(
            election_repository=self.election_repository(db=db)
        )


factory = Factory()