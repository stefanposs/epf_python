import asyncio
import os
import sys
sys.path.append(os.getcwd())
from lib.infrastructure.azure import azBlobClient
from lib.models.base import baseEvent
from lib.infrastructure.repository.base import baseRepository


class BronzeEventLayerRepository(baseRepository.BaseRepository):

    __azBlobClient: azBlobClient.AzBlobClient

    def __init__(
        self,
        azBlobClient: azBlobClient.AzBlobClient
    ):
        self.__azBlobClient = azBlobClient
    """
    getter/setter methods
    """

    def get_azBlobClient(self) -> azBlobClient.AzBlobClient:
        return self.__azBlobClient

    def set_azBlobClient(self, azBlobClient: azBlobClient.AzBlobClient) -> None:
        self.__azBlobClient = azBlobClient

    """
    methods
    """
    async def error(self, event: baseEvent.BaseEvent) -> None:
        loop = asyncio.get_event_loop()

        loop.run_until_complete(
            
            self.__azBlobClient.createBlob(
                fileName=event.meta.uuid,
                fileContent=str(event),
                container='machinetelemetry-bronze-error',
            )
            
        )


    async def processed(self, event: baseEvent.BaseEvent) -> None:
        loop = asyncio.get_event_loop()

        loop.run_until_complete(
            self.__azBlobClient.createBlob(
                fileName=event.meta.uuid,
                fileContent=str(event),
                container='machinetelemetry-bronze-processed',
            )
        )


    async def raw(self, event: baseEvent.BaseEvent) -> None:
        loop = asyncio.get_event_loop()

        loop.run_until_complete(
            self.__azBlobClient.createBlob(
                fileName=event.meta.uuid,
                fileContent=str(event),
                container='machinetelemetry-bronze-raw',
            )
        )
