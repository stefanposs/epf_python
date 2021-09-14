import os, sys
sys.path.append(os.getcwd())
import abc


class BaseRepository(abc.ABC):
    def __init__(self):
        raise NotImplementedError
