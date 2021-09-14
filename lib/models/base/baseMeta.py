import os
import sys

from pydantic.class_validators import validator

sys.path.append(os.getcwd())
from pydantic import BaseModel
from typing import List, Optional
from lib.models.base import baseSource
from lib.models.base import baseTarget
from lib.models.base import baseLayer


class BaseMeta(BaseModel):
    uuid: Optional[str]
    schemaVersion: int
    command: str
    source: baseSource.BaseSource
    target: Optional[baseTarget.BaseTarget]
    layer: Optional[List[baseLayer.BaseLayer]]

    @validator('uuid')
    def set_name(cls, uuid: str):
        if uuid is None:
            uuid = uuid.uuid4()
        return uuid

    @validator('command')
    def set_command(cls, command: str):
        if command is 'create' or ' delete' or 'update':
            return command
