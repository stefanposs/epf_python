import os, sys
sys.path.append(os.getcwd())
from pydantic import BaseModel
from lib.models.base.BaseData import BaseData


class Data(BaseData):
    pass