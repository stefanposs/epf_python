import os, sys
sys.path.append(os.getcwd())
import abc
import logging


class BaseLog(abc.ABC):

    def __init__(self):
        pass

    @staticmethod
    def info(
            className: str,
            msg: str
    ) -> None:
        raise NotImplementedError

    @staticmethod
    def error(
            className: str,
            msg: str
    ) -> None:
        raise NotImplementedError

    @staticmethod
    def warning(
            className: str,
            msg: str
    ) -> None:
        raise NotImplementedError

    @staticmethod
    def debug(
            className: str,
            msg: str
    ) -> None:
        raise NotImplementedError
