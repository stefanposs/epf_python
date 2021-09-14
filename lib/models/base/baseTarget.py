import os, sys
sys.path.append(os.getcwd())
import abc
from pydantic import BaseModel



class BaseTarget(BaseModel):
    domainName: str
    buildingBlock: str
    aggregate: str
    dataSchemaVersion: str
