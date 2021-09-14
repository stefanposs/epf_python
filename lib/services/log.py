import os, sys
sys.path.append(os.getcwd())
import logging


class Log:

    def __init__(self):
        pass

    @staticmethod
    def info(
            className: str,
            msg: str
    ) -> None:
        logging.info(className + ' : ' + msg)

    @staticmethod
    def error(
            className: str,
            msg: str
    ) -> None:
        logging.error(className + ' : ' + msg)

    @staticmethod
    def warning(
            className: str,
            msg: str
    ) -> None:
        logging.warning(className + ' : ' + msg)

    @staticmethod
    def debug(
            className: str,
            msg: str
    ) -> None:
        logging.debug(className + ' : ' + msg)
