import os, sys
sys.path.append(os.getcwd())
from azure.storage.blob.aio import BlobClient, BlobServiceClient
from lib.services import log


class AzBlobClient:
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
    __log: log.Log

    def __init__(
        self,
        conString: str,
    ):
        """
        Prints the person's name and age.

        If the argument 'additional' is passed, then it is appended after the main info.

        Parameters
        ----------
        additional : str, optional
            More info to be displayed (default is None)

        Returns
        -------
        None
        """
        self.__conString = conString
        self.__Logging = log.Log()

    """
    getter/setter methods
    """
    def get_conString(self) -> str:
        return self.__conString

    def set_conString(self, conString: str) -> str:
        self.__conString = conString

    async def createBlob(
        self,
        fileName: str,
        fileContent: str,
        container: str
    ) -> None:
        blobClient = BlobClient.from_connection_string(
            conn_str=self.__conString,
            container_name=container,
            blob_name=fileName
        )
        async with blobClient:
            try:
                await blobClient.upload_blob(
                    fileContent,
                    overwrite=True
                )
            except Exception as err:
                self.__log.error(str(__class__.__name__)+':'+str(err))

    async def deleteBlob(
        self,
        fileName: str,
        container: str,
    ) -> bool:
        blobServiceClient = BlobServiceClient.from_connection_string(
            conn_str=self.__conString
        )
        async with blobServiceClient:
            blobClient = blobServiceClient.get_blob_client(
                container,
                fileName,
                snapshot=None
            )
            try:
                blobData = await blobClient.delete_blob()
            except Exception as err:
                self.__log.error(str(err))

    async def updateBlob(
        self,
        fileName: str,
        fileContent: str,
        container: str,
    ) -> None:
        await self.createBlob(fileName=fileName, fileContent=fileContent, container=container)

    async def downloadBlob(
        self,
        fileName: str,
        container: str,
    ) -> str:
        blobServiceClient = BlobServiceClient.from_connection_string(
            conn_str=self.__conString
        )
        async with blobServiceClient:
            blobClient = blobServiceClient.get_blob_client(
                container,
                fileName,
                snapshot=None
            )
            try:
                blobData = await blobClient.download_blob()
                data = await blobData.content_as_text(
                    max_concurrency=3,
                    encoding='UTF-8'
                )
            except Exception as err:
                self.__log.error(str(err))
        return data
