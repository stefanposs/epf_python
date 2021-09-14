import os, sys

sys.path.append(os.getcwd())
from pydantic import BaseModel
from lib.models.base import baseMeta

class BaseEvent(BaseModel):
    data: dict
    meta: baseMeta.BaseMeta