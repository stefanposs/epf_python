import asyncio
import os
import sys
sys.path.append(os.getcwd())
from lib.infrastructure.azure.azBlobClient import AzBlobClient
from lib.models.base.baseEvent import BaseEvent
from lib.infrastructure.repository.base.baseRepository import BaseRepository


class BronzeEventLayerRepository(BaseRepository):

    __azBlobClient: AzBlobClient

    def __init__(
        self,
        azBlobClient: AzBlobClient
    ):
        if azBlobClient is not None:
            self.__azBlobClient = azBlobClient
        else:
            self.__azBlobClient = None
    """
    getter/setter methods
    """
    def get_azBlobClient(self) -> AzBlobClient:
        return self.__azBlobClient

    def set_azBlobClient(self, azBlobClient: AzBlobClient) -> None:
        self.__azBlobClient = azBlobClient

    """
    methods
    """
    async def error(self, event: BaseEvent) -> None:
        loop = asyncio.get_event_loop()

        loop.run_until_complete(
            
            self.__azBlobClient.createBlob(
                fileName=event.meta.uuid,
                fileContent=str(event.json()),
                container='machinetelemetry-bronze-error',
            )

            
        )

    async def processed(self, event: BaseEvent) -> None:

            await self.__azBlobClient.createBlob(
                fileName=event.meta.uuid,
                fileContent=str(event.json()),
                container='machinetelemetry-bronze-processed',
            )


    async def raw(self, event: BaseEvent) -> None:

            await self.__azBlobClient.createBlob(
                fileName=event.meta.uuid,
                fileContent=str(event.json()),
                container='machinetelemetry-bronze-raw',
            )



