from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, fields

from do.customer_do import CustomerDo
from service.customer_service import CustomerService
from app import api
customer_ns = Namespace("customer", description="顾客信息")

customer_service = CustomerService()


@customer_ns.route("/")
class CustomerController(Resource):
    # 鉴权操作
    # decorators = [jwt_required()]
    customer_get_parser = api.parser()
    customer_get_parser.add_argument("id", type=int, location="args")

    @customer_ns.expect(customer_get_parser)
    def get(self):
        """
        顾客信息的查找
        :return:
        """
        id = request.args.get("id")
        name = request.args.get("name")
        page = int(request.args.get("page")) if request.args.get("page") else 1
        limit = int(request.args.get("limit")) if request.args.get("limit") else 20
        if id:
            # 如有有id则进行数据查找
            data = customer_service.get(id)
            if data:
                # 如果查到数据，则返回给前端
                datas = [data.as_dict()]
                return {"code": 0, "msg": "data success get", "data": {"list": datas, "count": len(datas)}}
            else:
                # 如果没有数据，则返回数据不存在
                return {"code": 40004, "msg": "data is not exists"}
        elif name:
            data = customer_service.get_by_name(name)
            if data:
                # 如果查到数据，则返回给前端
                datas = [data.as_dict()]
                return {"code": 0, "msg": "data success get", "data": {"list": datas, "count": len(datas)}}
            else:
                # 如果没有数据，则返回数据不存在
                datas = []
                return {"code": 0, "msg": "data is not exists", "data": {"list": datas, "count": len(datas)}}
        else:
            # 如果没有id,则返回全部数据
            datas = [testcase.as_dict() for testcase in customer_service.list()]
            res_datas = [datas[i:i + limit] for i in range(0, len(datas), limit)]
            return {"code": 0, "msg": "data success get", "data": {"list": res_datas[page - 1], "count": len(datas)}}

    customer_post_model = customer_ns.model("customer_post_model", {
        "name": fields.String,
        "addr": fields.String,
        "age": fields.Integer,
        "birth": fields.String,
        "sex": fields.String
    })

    @customer_ns.expect(customer_post_model)
    def post(self):
        """
        顾客信息的新增
        :return:
        """
        data = request.json
        # data -> {a=1, b=2} ==> a=1, b=2
        customer = CustomerDo(**data)
        # 新增用户
        customer_id = customer_service.save(customer)
        if customer_id:
            # 存在测试用例id,则证明用例新增成功了
            return {"code": 0, "msg": f"{customer_id} success add"}
        else:
            return {"code": 40001, "msg": "customer is exists"}

    customer_put_model = customer_ns.model("customer_put_model", {
        "id": fields.Integer,
        "name": fields.String,
        "addr": fields.String,
        "age": fields.Integer,
        "birth": fields.String,
        "sex": fields.String
    })

    @customer_ns.expect(customer_put_model)
    def put(self):
        """
        顾客信息的更新
        :return:
        """
        data = request.json
        customer = CustomerDo(**data)
        customer_id = customer_service.update(customer)
        if customer_id:
            # 存在顾客id,则证明修改成功了
            return {"code": 0, "msg": f"{customer_id} success update"}
        else:
            return {"code": 40001, "msg": "customer is not exists"}

    customer_delete_parser = api.parser()
    customer_delete_parser.add_argument("id", type=int, location="json", required=True)

    @customer_ns.expect(customer_delete_parser)
    def delete(self):
        """
        顾客信息的删除
        :return:
        """
        # data ==> {"id": 1}
        id = request.args.get("id")
        print(f"data:{id}")
        # 删除用例
        customer_id = customer_service.delete(id)
        if customer_id:
            # 存在顾客id,则证明删除成功了
            return {"code": 0, "msg": f"{customer_id} success delete"}
        else:
            return {"code": 40001, "msg": "customer_id is not exists"}