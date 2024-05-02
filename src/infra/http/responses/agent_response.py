from ....domain.entities.traffic_agent import AccountProps






class Responses:
    def return_datas(datas: any):
        """create response for agent account"""
        instance_model = AccountProps(
            username=datas[0],
            email=datas[1],
            password=" ",
            cellphone=datas[2]
        ).model_dump()
        instance_model.pop("password")
        return instance_model
