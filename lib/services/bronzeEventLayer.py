import collections
import os
import sys
import uuid
import datetime

from jsonschema import validate
from jsonschema import Draft7Validator



sys.path.append(os.getcwd())
from pydantic import json
from lib.models.base.baseLayer import BaseLayer
from lib.infrastructure.repository import bronzeEventLayerRepository
from lib.services.base.baseEventLayer import BaseEventLayer
from lib.models.base.baseEvent import BaseEvent
from lib.services.log import Log


class BronzeEventLayer(BaseEventLayer):
    __inputSchema: json
    __outputSchema: json
    __processLayerRepository: bronzeEventLayerRepository
    __log: Log

    def __init__(
        self,
        inputSchema: json,
        outputSchema: json,
        processLayerRepository: bronzeEventLayerRepository
    ):
        self.__inputSchema = inputSchema
        self.__outputSchema = outputSchema
        self.__processLayerRepository = processLayerRepository
        self.__log = Log()

    """
    getter/setter methods
    """
    def get_inputSchema(self) -> json:
        return self.__inputSchema

    def set_inputSchema(self, inputSchema: json) -> None:
        self.__inputSchema = inputSchema

    def get_outputSchema(self) -> json:
        return self.__outputSchema

    def set_outputSchema(self, outputSchema: json) -> None:
        self.__outputSchema = outputSchema

    def isInputValid(self, inputEvent: BaseEvent) -> bool:
        res = False
        if self.__isValid(event=inputEvent, schema=self.__inputSchema):
            res = True
        return res

    def isOutputValid(self, outputEvent: BaseEvent) -> bool:
        res = False
        if self.__isValid(event=outputEvent, schema=self.__outputSchema):
            res = True
        return res

    async def process(self, event: BaseEvent, msg: str) -> None:
        if event.meta.uuid is None:
            event.meta.uuid = str(uuid.uuid4())
        if event.meta.layer is None:
            event.meta.layer = []
        self.__log.info(
            "getLabel()",
            str(event.meta.layer)
        )
        event.meta.layer.append(
            BaseLayer(
                name='.' + __name__ + '.' + 'BronzeEventLayer',
                entryTimeStampUtc=str(datetime.datetime.utcnow().isoformat()[:-3] + 'Z'),
                message=msg
            )
        )
        await self.__processLayerRepository.raw(event=event)
        await self.__processLayerRepository.processed(event=event)

    async def error(self, event: BaseEvent, msg: str) -> None:
        if event.meta.uuid is None:
            event.meta.uuid = str(uuid.uuid4())
        if event.meta.layer is None:
            event.meta.layer = []
        self.__log.info(
            "getLabel()",
            str(event.meta.layer)
        )
        event.meta.layer.append(
            BaseLayer(
                name='.' + __name__ + '.' + 'BronzeEventLayer',
                entryTimeStampUtc=str(datetime.datetime.utcnow().isoformat()[:-3] + 'Z'),
                message=msg
            )
        )
        await self.__processLayerRepository.error(event=event)
    def __isValid(self, event: BaseEvent, schema: json) -> bool:
        res = False
        try:
            if validate(instance=event, schema=dict(schema)) is None:
                res = True
        except Exception as err:
            self.__log.error(
                "getLabel()",
                str(err)
            )
            res = False
        return res

    def MetaAddLayerEnquedTime(self, event: BaseEvent) -> bool:
        res = False
        return res
