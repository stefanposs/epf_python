import os
import sys
from jsonschema import validate
from jsonschema import Draft7Validator
sys.path.append(os.getcwd())
from pydantic import json
from lib.infrastructure.repository import bronzeEventLayerRepository
from lib.services.base import baseEventLayer
from lib.models.base import baseEvent
from lib.services import log


class BronzeEventLayer(baseEventLayer.BaseEventLayer):
    __inputSchema: json
    __outputSchema: json
    __processLayerRepository: bronzeEventLayerRepository
    __log: log.Log

    def __init__(
        self,
        inputSchema: json,
        outputSchema: json,
        processLayerRepository: bronzeEventLayerRepository
    ):
        self.__inputSchema = inputSchema
        self.__outputSchema = outputSchema
        self.__processLayerRepository = processLayerRepository

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

    def isInputValid(self, inputEvent: baseEvent.BaseEvent) -> bool:
        res = False
        return res

    def isOutputValid(self, outputEvent: baseEvent.BaseEvent) -> bool:
        res = False
        if self.__isValid(event=outputEvent, schema=self.__inputSchema):
            res = True
        return res

    def __isValid(self, event: baseEvent.BaseEvent, schema: json) -> bool:
        res = False
        try:
            if validate(instance=event, schema=self.schema) is None:
                res = True
        except Exception as err:
            self.__log.error(
                "getLabel()",
                str(err)
            )
            res = False
        return res

    def MetaAddLayerEnquedTime(self, event: baseEvent.BaseEvent) -> bool:
        res = False
        return res
