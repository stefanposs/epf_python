import os, sys

sys.path.append(os.getcwd())
from pydantic import BaseModel
from lib.models.base.baseMeta import BaseMeta

class BaseEvent(BaseModel):
    data: dict
    meta: BaseMeta