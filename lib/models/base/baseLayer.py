import os
import sys
sys.path.append(os.getcwd())
from pydantic import BaseModel

class BaseLayer(BaseModel):
    name: str
    entryTimeStampUtc: str
    message: str

