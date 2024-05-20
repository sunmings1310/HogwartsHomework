from flask import request
from flask_restx import Namespace, Resource, fields

from do.user_do import UserDo
from service.user_service import UserService

user_ns = Namespace("user", description="用户管理")

user_service = UserService()


@user_ns.route("/login")
class LoginController(Resource):

    login_post_model = user_ns.model("login_post_model", {
        "username": fields.String,
        "password": fields.String
    })

    @user_ns.expect(login_post_model)
    def post(self):
        """
        登录功能
        :return:
        """
        user_info = request.json
        # 通过用户名和密码生成user对象
        user = UserDo(**user_info)
        print(f"user: {user}")
        # 通过用户名查找用户是否存在
        user_result = user_service.get_by_name(user.username)
        print(f"user_result: {user_result}")
        if not user_result:
            # 如果用户不存在，说明用户还没有注册
            return {"code": 40013, "msg": "用户未注册"}
        if not user_result.check_hash_password(user_info.get("password")):
            # 如果密码不匹配
            return {"code": 40014, "msg": "密码错误"}
        # 用户存在，且密码正确，则生成token
        access_token = user_service.create_access_token(user_result.as_dict())
        if access_token:
            # 存在access_token,则证明登录成功了
            return {"code": 0, "msg": "登录成功", "data": {"token": access_token}}
        else:
            return {"code": 40021, "msg": "登录失败"}

    @user_ns.route("/register")
    class RegisterController(Resource):

        register_post_model = user_ns.model("register_post_model", {
            "username": fields.String,
            "password": fields.String,
        })

        @user_ns.expect(register_post_model)
        def post(self):
            """
            注册功能
            :return:
            """
            data = request.json
            user = UserDo(**data)
            # 新增
            user_id = user_service.save(user)
            print(f"user_id: {user_id}")
            if user_id:
                # 存在id,则证明新增成功了
                return {"code": 0, "msg": f"{user_id} success add"}
            else:
                return {"code": 40001, "msg": "case is exists"}