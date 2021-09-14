import os, sys
sys.path.append(os.getcwd())
import os, sys
sys.path.append(os.getcwd())
import abc


class BaseEventLayer(abc.ABC):

    def __init__(self):
        raise NotImplementedError

    @abc.abstractmethod
    def isInputValid(self) -> bool:
        raise NotImplementedError

    @abc.abstractmethod
    def isOutputValid(self) -> bool:
        raise NotImplementedError

    @abc.abstractmethod
    def MetaAddLayerEnquedTime(self) -> bool:
        raise NotImplementedError
