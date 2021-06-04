"""Main module."""

from sciencewriter.informationmodel import SciencePaper, AuthorInfo
from sciencewriter._api import *

class ScienceWriterApp():
    """This class represents the application as a whole that exposes the API for other derived works to access and to manipulate the internals of the writing project.
    """
    def __init__(self) -> None:
        self.papers:list[SciencePaper] = None
        self.location:str = None
        self.author_infos:dict[str,AuthorInfo] = None
        pass

    def persist_information(self):
        """This function takes the internal state of the application and persists it to a location from where it can be instantiated at a later time.
        """
        pass

    def reload_information(self):
        """This function takes an information state persisted at some location and it will instantiate the application based on that information.
        """
        pass

