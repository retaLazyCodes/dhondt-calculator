from typing import Any, Generic, Type, TypeVar

from core.database import Base
from core.exceptions import NotFoundException
from core.repository import BaseRepository

ModelType = TypeVar("ModelType", bound=Base) # type: ignore

class BaseController(Generic[ModelType]):
    """Base class for data controllers."""

    def __init__(self, model: Type[ModelType], repository: BaseRepository):
        self.model_class = model
        self.repository = repository

    def get_all(
        self, skip: int = 0, limit: int = 100, order_: dict | None = None
    ) -> list[ModelType]:
        """
        Returns a list of records based on pagination params.

        :param skip: The number of records to skip.
        :param limit: The number of records to return.
        :param order_: The order of the results. (e.g desc, asc).
        :return: A list of records.
        """
        return self.repository.get_all(skip, limit, order_)

    def create(self, attributes: dict[str, Any]) -> ModelType:
        """
        Creates a new Object in the DB.

        :param attributes: The attributes to create the object with.
        :return: The created object.
        """
        return self.repository.create(attributes)

