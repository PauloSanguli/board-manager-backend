"""interface for owner repository manager"""

from abc import ABC, abstractmethod



class IOwnerRepository(ABC):
    @abstractmethod
    def create():
        """insert owner in database"""
        raise NotImplementedError("implement the method create")

    @abstractmethod
    def get_all():
        """get all owners from database"""
        raise NotImplementedError("implement the method get_all")
    
    @abstractmethod
    def get_by_veichle():
        """get owner by veichle"""
        raise NotImplementedError("implement the method get_by_veichle")

    @abstractmethod
    def login():
        """login for owner"""
        raise NotImplementedError("implement the method login")    
