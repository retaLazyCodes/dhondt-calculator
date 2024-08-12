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

    def get(self, id_: int, join_: set[str] | None = None) -> ModelType:
        """Returns the model instance matching the id."""

        db_obj = self.repository.get(id_, join_)
        if not db_obj:
            raise NotFoundException(
                f"{self.model_class.__tablename__.title()} with id: {id_} does not exist"
            )

        return db_obj

    def get_multi(
        self, skip: int = 0, limit: int = 100, join_: set[str] | None = None
    ) -> list[ModelType]:
        """Returns a list of models based on pagination params."""
        return self.repository.get_multi(skip, limit, join_)

    def create(self, attributes: dict[str, Any]) -> ModelType:
        """Creates a new Sqlalchemy Object"""
        return self.repository.create(attributes)

