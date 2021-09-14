import os, sys
sys.path.append(os.getcwd())
import json
import os

from azure.cosmos import CosmosClient, PartitionKey

from lib.services import log


class AzCosmosDbSqlClient:
    """
    A class to represent a person.

    ...

    Attributes
    ----------
    name : str
        first name of the person
    surname : str
        family name of the person
    age : int
        age of the person

    Methods
    -------
    info(additional=""):
        Prints the person's name and age.
    """
    __conString: str
    __containerName: str
    __databaseName: str
    __log: log.Log

    def __init__(
        self,
        conString: str,
        containerName: str,
        databaseName: str,
    ):
        self.__conString = conString
        self.__containerName = containerName
        self.__databaseName = databaseName
        self.__log = log.Log()

    """
    getter/setter methods
    """
    def get_conString(self) -> str:
        return self.__conString

    def set_conString(self, conString: str) -> str:
        self.__conString = conString

    def get_containerName(self) -> str:
        return self.__containerName

    def set_containerName(self, containerName: str) -> str:
        self.__containerName = containerName

    def get_databaseName(self) -> str:
        return self.__databaseName

    def set_databaseName(self, databaseName: str) -> str:
        self.__databaseName = databaseName

    async def containerExist(self) -> bool:
        res = False
        try:
            client = CosmosClient.from_connection_string(self.__conString)
            database = client.create_database_if_not_exists(id=self.__databaseName)
            database.create_container_if_not_exists(
                id=self.__containerName,
                partition_key=PartitionKey(path="/meta/uuid")
            )
            res = True
        except Exception as err:
            self.__log.error(
                str(__class__.__name__),
                str(err)
            )
            res = False
        return res

    async def databaseExist(self) -> bool:
        res = False
        try:
            client = CosmosClient.from_connection_string(self.__conString)
            client.create_database_if_not_exists(id=self.__databaseName)
            res = True
        except Exception as err:
            self.__log.error(
                str(__class__.__name__),
                str(err)
            )
            res = False
        return res

    async def itemExist(
            self,
            itemId: str,
    ) -> bool:
        res = False
        try:
            client = CosmosClient.from_connection_string(self.__conString)
            database = client.get_database_client(database=self.__databaseName)
            container = database.get_container_client(container=self.__containerName)
            container.read_item(item=itemId, partition_key=itemId)
            res = True
        except Exception as err:
            self.__log.error(
                str(__class__.__name__),
                str(err)
            )
            res = False
        return res

    async def createItem(
        self,
        itemId: str,
        itemContent: str,
    ) -> bool:
        res = False
        try:
            client = CosmosClient.from_connection_string(self.__conString)
            database = client.get_database_client(database=self.__databaseName)
            container = database.get_container_client(container=self.__containerName)
            item = json.loads(itemContent)
            item.update({'id': itemId})
            container.create_item(body=item)
            res = True
        except Exception as err:
            self.__log.error(
                str(__class__.__name__),
                str(err)
            )
            res = False
        return res


    async def deleteItemById(
        self,
        itemId: str,
    ) -> bool:
        res = False
        try:
            client = CosmosClient.from_connection_string(self.__conString)
            database = client.get_database_client(database=self.__databaseName)
            container = database.get_container_client(container=self.__containerName)
            container.delete_item(item=itemId, partition_key=itemId)
            res = True
        except Exception as err:
            self.__log.error(
                str(__class__.__name__),
                str(err)
            )
            res = False
        return res

    async def replaceItemById(
        self,
        itemId: str,
        itemContent: str,
    ) -> None:
        res = False
        try:
            client = CosmosClient.from_connection_string(self.__conString)
            database = client.get_database_client(database=self.__databaseName)
            container = database.get_container_client(container=self.__containerName)
            item = json.loads(itemContent)
            item.update({'id': itemId})
            container.replace_item(item=itemId, body=item)
            res = True
        except Exception as err:
            self.__log.error(
                str(__class__.__name__),
                str(err)
            )
            res = False
        return res

    def queryItem(
            self,
            query: str,
    ) -> None:
        pass

    def queryItemById(
        self,
        query: str,
    ) -> None:
        pass
