import os, sys
sys.path.append(os.getcwd())
from lib.services.log import Log


class AzSqlClient:
    __conString: str
    __containerName: str
    __log: Log

    def __init__(
            self,
            conString: str,
            containerName: str,
    ):
        self.__conString = conString
        self.__containerName = containerName
        self.__log = Log()

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
