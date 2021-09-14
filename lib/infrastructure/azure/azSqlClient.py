import os, sys
sys.path.append(os.getcwd())
from lib.services import log


class AzSqlClient:
    __conString: str
    __containerName: str
    __log: log

    def __init__(
            self,
            conString: str,
            containerName: str,
    ):
        self.__conString = conString
        self.__containerName = containerName

    async def insert(
            self,
            fileName: str,
            fileContent: str,
    ) -> None:
        pass

    def delete(
            self,
            fileName: str,
    ) -> None:
        pass

    def update(
            self,
            fileName: str,
            fileContent: str,
    ) -> None:
        pass

    def select(
            self,
            query: str,
    ) -> None:
        pass
