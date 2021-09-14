import os, sys
sys.path.append(os.getcwd())
from lib.infrastructure.repository.base.baseRepository import BaseRepository

class GoldEventLayerRepository(BaseRepository):
    def __init__(self):
        raise NotImplementedError

    async def error(self) -> None:
        raise NotImplementedError

    async def process(self) -> None:
        raise NotImplementedError

    async def raw(self, reference) -> None:
        raise NotImplementedError
