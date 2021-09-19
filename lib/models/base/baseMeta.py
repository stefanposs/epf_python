import os
import sys

from pydantic.class_validators import validator
import uuid as ui
sys.path.append(os.getcwd())
from pydantic import BaseModel
from typing import List, Optional
from lib.models.base.baseSource import BaseSource
from lib.models.base.baseTarget import BaseTarget
from lib.models.base.baseLayer import BaseLayer


class BaseMeta(BaseModel):
    uuid: Optional[str]
    schemaVersion: int
    command: str
    source: BaseSource
    target: Optional[BaseTarget]
    layer: Optional[List[BaseLayer]]

    @validator('uuid')
    def set_uuid(cls, uuid: str):
        if uuid is None:
            uuid = ui.uuid4()
        return uuid

    @validator('command')
    def set_command(cls, command: str):
        if command == 'create' or command == ' delete' or command == 'update':
            return command
