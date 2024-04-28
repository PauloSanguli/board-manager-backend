from pydantic import BaseModel

from typing import Type
from datetime import date



class DrivingLicenseProps(BaseModel):
    """driving license fields"""
    name: str
    issue_date: date
    expiration_date: date
    category_veichle: str
    restrictions: str
    veichle_identification_number: int
    document_issuer_signature: str
    expired: bool



class DrivingLicenseMap:
    def __init__(self, driving_license: DrivingLicenseProps):
        """create the schema of driving license"""
        self.__driving_license = {
            "name": driving_license.name,
            "issue_date": driving_license.issue_date,
            "expiration_date": driving_license.expiration_date,
            "category_veichle": driving_license.category_veichle,
            "restrictions": driving_license.restrictions,
            "veichle_identification_number": driving_license.veichle_identification_number,
            "document_issuer_signature": driving_license.document_issuer_signature,
            "expired": driving_license.expired
        }
    
    def get_dic(self) -> dict:
        """return the schema"""
        return self.__driving_license.copy()
        
        
        
        
        
        
        
