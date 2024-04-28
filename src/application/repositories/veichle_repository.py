"""interface for repositorys veichles""" 

from abc import ABC, abstractmethod




class IVeichleRepository(ABC):
    @abstractmethod
    def create():
        """insert the veichle in db"""
        raise NotImplementedError("implement the method create")
    
    @abstractmethod
    def get_all():
        """get all veichles from db"""
        raise NotImplementedError("implement the method get_all")

    @abstractmethod
    def get_by_board():
        """get veichle by the board"""
        raise NotImplementedError("implement the method get_by_board")

    @abstractmethod
    def get_id_by_board():
        """get car veichle title or blocket id by the board"""
        raise NotImplementedError("implment the method get_id_by_board")
        
    @abstractmethod
    def get_datas_by_board_picture():
        """get datas of user and veichle by board from picture"""
        raise NotImplementedError("implement the method get_datas_by_board_picture")
    
    @abstractmethod
    def regist_infraction_veichle(infraction_info: dict):
        """regist infraction of an user and car"""
        raise NotImplementedError("implement the method regist_infraction_veichle")
    
    @abstractmethod
    def get_infractions():
        raise NotImplementedError("implement the method get_infractions")
    
    # @abstractmethod
    # def update_state():
    #     raise NotImplementedError("implement the method update_state")
