import os
import sys
sys.path.append(os.getcwd())
import abc
from pydantic import BaseModel

class BaseLayer(BaseModel):
    name: str
    entryTimeStampUtc: str
    message: str

