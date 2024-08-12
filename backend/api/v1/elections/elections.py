from typing import Optional
from fastapi import APIRouter, Depends, Query

from app.schemas import ElectionRequest, ElectionResponse
from app.controllers import ElectionController
from core.factory import Factory

election_router = APIRouter()


@election_router.get("/")
def get_elections(
    election_cotroller: ElectionController = Depends(Factory().get_election_controller),
    order: Optional[str] = Query(None, description="Order by 'asc' or 'desc'"),
) -> list[ElectionResponse]:
    """
    Retrieves a list of elections with optional ordering.

    :param election_controller: Dependency that provides the ElectionController.
    :param order: Optional query parameter to specify the order ('asc' or 'desc'). Defaults to 'asc' by 'id'.
    :return: A list of ElectionResponse.
    """
    if order == "desc":
        order_criteria = {
            "desc": ["id"]
        }
    else:
        order_criteria = {
            "asc": ["id"]
        }
    return election_cotroller.get_all(order_=order_criteria)


@election_router.post("/")
def create_election(
    create_election_request: ElectionRequest,
    election_cotroller: ElectionController = Depends(Factory().get_election_controller),
) -> ElectionResponse:
    """
    Insert an Election object in Database and retrieves it.

    :param create_election_request: The request body containing the number of seats and votes. 
    :param election_controller: Dependency that provides the ElectionController.
    :return: A ElectionResponse object.
    """
    return election_cotroller.register_calculation(
        seats=create_election_request.seats,
        votes=create_election_request.votes,
    )