from .fields_entities import (
    CAR_VEICHLE_TITLE_FIELDS,BLOCKET_FIELDS,DOCS_FIELDS
)

from ....domain.entities.infractions import InfractionsProps




class Responses:
    def get_all():
        """"""
    
    def get_one(datas):
        """join the docs schemas and retunr"""
        doc_blocket = datas[1:18]
        doc_car_veichcle_title = datas[18:33]

        response = {
            "veichle_id": datas[-1],
            "blocket": Responses.schema_docs(doc_blocket, BLOCKET_FIELDS),
            "car_veichle-title": Responses.schema_docs(doc_car_veichcle_title, CAR_VEICHLE_TITLE_FIELDS),
            "secure": Responses.docs(datas,33),
            "license": Responses.docs(datas,36),
            "inspection": Responses.docs(datas,39)
        }
        return response
    
    def schema_docs(object_map, fields_list):
        """create the schema of blocket and car veichle tittle"""
        __schema_blocket = {}
        for index, field in enumerate(fields_list):
            __schema_blocket[f"{field}"] = object_map[index]
        return __schema_blocket

    #secure-33=35 | license-36=38 | inspection-39=41
    def docs(object_map, init: int):
        """create the schema of docs"""
        __doc = {}
        index = init
        for field in DOCS_FIELDS:
            __doc[f"{field}"] = object_map[index]
            index+=1
        return __doc
    
    def get_infractions(datas: list)        :
        """create scheme of nfractions"""
        response = []
        
        for __infraction in datas:
            instance_model = InfractionsProps(
                    num_carter_habilitacion=__infraction[0],
                    obs=__infraction[1],
                    date=__infraction[2],
                    local=__infraction[3],
                    time=__infraction[4],
                    type_infraction=__infraction[5],
                    value=__infraction[6],
                    info_payment=__infraction[7],
                    paid=__infraction[8],
                    id=__infraction[9]
                ).model_dump()
            instance_model.pop("board")
            response.append(
                instance_model
            )
        return response
