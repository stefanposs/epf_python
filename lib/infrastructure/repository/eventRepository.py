import os, sys
sys.path.append(os.getcwd())
from lib.infrastructure.repository.base.baseRepository import BaseRepository

class EventRepository(BaseRepository):
    def __init__(self):
        raise NotImplementedError

    async def create(self) -> None:
        raise NotImplementedError

    async def delete(self) -> None:
        raise NotImplementedError

    async def get(self, reference) -> None:
        raise NotImplementedError
