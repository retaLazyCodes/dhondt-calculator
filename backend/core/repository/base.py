from typing import Any, Generic, Type, TypeVar

from sqlalchemy import Select
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import select as sqla_select

from core.database import Base


ModelType = TypeVar("ModelType", bound=Base) # type: ignore


class BaseRepository(Generic[ModelType]):
    def __init__(self, db: Session, model: Type[ModelType]):
        self.db = db
        self.model_class: Type[ModelType] = model

    def create(self, attributes: dict[str, Any] = None) -> ModelType:
        """Creates the model instance."""
        if not attributes:
            attributes = {}

        model = self.model_class(**attributes)
        self.db.add(model)

        return model

    def get_multi(
        self, skip: int = 0, limit: int = 100, join_: set[str] | None = None
    ) -> list[ModelType]:
        """Returns a list of models based on pagination params."""
        select = self._callable(join_)
        select = select.offset(skip).limit(limit)

        return self._all(select)

    def _callable(
        self,
        join_: set[str] | None = None,
        order_: dict | None = None,
    ) -> Select:
        """Returns a callable that can be used to query the model."""
        select = sqla_select(self.model_class)
        select = self._maybe_ordered(select, order_)

        return select

    def _all(self, select: Select) -> list[ModelType]:
        """Returns all results from the query."""
        return self.db.scalars(select).all()

    def _maybe_ordered(self, select: Select, order_: dict | None = None) -> Select:
        """Returns the query ordered by the given column."""
        if order_:
            if order_["asc"]:
                for order in order_["asc"]:
                    select = select.order_by(getattr(self.model_class, order).asc())
            else:
                for order in order_["desc"]:
                    select = select.order_by(getattr(self.model_class, order).desc())

        return select