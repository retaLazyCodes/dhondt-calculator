from app.models import Election
from core.repository import BaseRepository


class ElectionRepository(BaseRepository[Election]):
    """
    Election repository provides all the database operations for the Election model.
    """
    pass