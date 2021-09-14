import os, sys
sys.path.append(os.getcwd())
from pydantic import json
from lib.infrastructure.repository.base.baseRepository import BaseRepository
from lib.models.base.baseEvent import BaseEvent
from lib.services.base.baseEventLayer import BaseEventLayer


class SilverEventLayer(BaseEventLayer):
    __inputSchema: json
    __inputEvent: BaseEvent
    __outputSchema: json
    __outputEvent: BaseEvent
    __processLayerRepository: BaseRepository

    def __init__(
        self,
        inputSchema: json,
        inputEvent: BaseEvent,
        outputSchema: json,
        processLayerRepository: BaseRepository
    ):
        self.__inputSchema = inputSchema
        self.__inputEvent = inputEvent
        self.__outputSchema = outputSchema

    """
    getter/setter methods
    """
    def get_inputSchema(self) -> json:
        return self.__inputSchema

    def set_inputSchema(self, inputSchema: json) -> None:
        self.__inputSchema = inputSchema

    def get_inputEvent(self) -> BaseEvent:
        return self.__inputEvent

    def set_inputEvent(self, inputEvent: BaseEvent) -> None:
        self.__inputEvent = inputEvent

    def get_outputSchema(self) -> json:
        return self.__outputSchema

    def set_outputSchema(self, outputSchema: json) -> None:
        self.__outputSchema = outputSchema

    def isInputValid(self) -> bool:
        res = False
        return res

    def isOutputValid(self) -> bool:
        res = False
        return res

    def addMetaInformation(self) -> bool:
        res = False
        return res
