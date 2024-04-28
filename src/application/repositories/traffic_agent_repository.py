"""interface for repository of agents"""
from abc import ABC, abstractmethod



class ITrafficAgentRepository(ABC):
    @abstractmethod
    def create():
        """method for insert agent in db"""
        raise NotImplementedError("implement the method create")
    
    @abstractmethod
    def login():
        """login agent"""
        raise NotImplementedError("implement the method login")
    
    @abstractmethod
    def get_all():
        """get all agents from db"""
        raise NotImplementedError("implement the method get_all")
    
    @abstractmethod
    def get_by_number():
        """get a agent from the number"""
        raise NotImplementedError("implement the method get_by_number")
    
    @abstractmethod
    def get_infractions(board_car: str):
        """get infractions of an veichle"""
        raise NotImplementedError("implement the method get_infractions")
