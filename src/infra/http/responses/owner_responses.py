from .fields_entities import IDENTITY_CARD_FIELDS, DRIVING_LICENSE_FIELDS

from ....domain.entities.driving_license import DrivingLicenseProps





class Responses:
    """responses for owner datas"""
    def get_all(datas: any):
        """return all"""

        owners = []
        for owner in datas:
            owners.\
                append(Responses.__create_dic(owner))
        return owners
    
    def __union_docs():
        """join identity card fields and driving license fields"""
        doc = []
        for field_ in IDENTITY_CARD_FIELDS:
            doc.append(field_)
        for field_ in DRIVING_LICENSE_FIELDS:
            doc.append(field_)
        return doc
    
    def get_one(datas: any):
        """return a response model"""
        return Responses.__create_dic(datas)
    
    def __create_dic(owner: any):
        """create the dic response"""

        response_dic_card = {
            "identity_card": {},
            "driving_license": {}
        }
        next_index = 0
        for index in range(0,len(IDENTITY_CARD_FIELDS)):
            response_dic_card["identity_card"][f"{IDENTITY_CARD_FIELDS[index]}"] = owner[index]
            next_index = index
        next_index+=1
        for index in range(0, len(DRIVING_LICENSE_FIELDS)):
            response_dic_card["driving_license"][f"{DRIVING_LICENSE_FIELDS[index]}"] = owner[next_index]
            next_index+=1
        response_dic_card["owner_id"] = owner[-1]
        
        return response_dic_card
    
    def get_driving_license(datas: any):
        """create the dic response of dricing license"""
        response = DrivingLicenseProps(
            name=datas[0],
            issue_date=datas[1],
            expiration_date=datas[2],
            category_veichle=datas[3],
            restrictions=datas[4],
            veichle_identification_number=datas[5],
            document_issuer_signature=datas[6],
            expired=datas[7]
        ).model_dump()
        return response
