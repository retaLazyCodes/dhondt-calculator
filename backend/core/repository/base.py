from typing import Any, Generic, Type, TypeVar

from sqlalchemy import Select
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import select as sqla_select

from core.database import Base


ModelType = TypeVar("ModelType", bound=Base) # type: ignore


class BaseRepository(Generic[ModelType]):
    """Base class for data repositories."""

    def __init__(self, model: Type[ModelType], db: Session):
        self.db = db
        self.model_class: Type[ModelType] = model

    def create(self, attributes: dict[str, Any] = None) -> ModelType:
        """
        Creates the model instance.

        :param attributes: The attributes to create the model with.
        :return: The created model instance.
        """
        if not attributes:
            attributes = {}

        model = self.model_class(**attributes)
        self.db.add(model)
        self.db.commit()

        return model

    def get_all(
        self, skip: int = 0, limit: int = 100, order_: dict | None = None
    ) -> list[ModelType]:
        """
        Returns a list of model instances.

        :param skip: The number of records to skip.
        :param limit: The number of record to return.
        :param order_: The order of the results. (e.g desc, asc).
        :return: A list of model instances.
        """
        query = self._query(order_)
        query = query.offset(skip).limit(limit)

        return self._all(query)

    def _query(
        self,
        order_: dict | None = None,
    ) -> Select:
        """
        Returns a callable that can be used to query the model.

        :param join_: The joins to make.
        :param order_: The order of the results. (e.g desc, asc)
        :return: A callable that can be used to query the model.
        """
        query = sqla_select(self.model_class)
        query = self._maybe_ordered(query, order_)

        return query

    def _all(self, query: Select) -> list[ModelType]:
        """
        Returns all results from the query.

        :param query: The query to execute.
        :return: A list of model instances.
        """
        return self.db.scalars(query).all()

    def _maybe_ordered(self, query: Select, order_: dict | None = None) -> Select:
        """
        Returns the query ordered by the given column.

        :param query: The query to order.
        :param order_: The order to make.
        :return: The query ordered by the given column.
        """
        if order_:
            if order_.get("asc"):
                for order in order_["asc"]:
                    query = query.order_by(getattr(self.model_class, order).asc())
            else:
                for order in order_["desc"]:
                    query = query.order_by(getattr(self.model_class, order).desc())

        return query