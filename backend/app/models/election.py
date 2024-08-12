from sqlalchemy import Column, Integer, JSON
from core.database import Base
from core.database.mixins import TimestampMixin

class Election(Base, TimestampMixin):
    __tablename__ = "election_results"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    seats = Column(Integer, nullable=False)
    votes = Column(JSON, nullable=False)
    results = Column(JSON, nullable=False)
