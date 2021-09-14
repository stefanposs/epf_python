import os, sys
sys.path.append(os.getcwd())
import abc
from pydantic import BaseModel



class BaseSource(BaseModel):
    uuid: str
    name: str
    dataType: str
    dateOfBirthUtc: str
    dataSchemaVersion: int
