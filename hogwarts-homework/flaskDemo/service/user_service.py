from flask_jwt_extended import create_access_token

from dao.user_dao import UserDao
from do.user_do import UserDo
from app import jwt

user_dao = UserDao()


class UserService:

    def get(self, user_id):
        # 通过id查询数据
        return user_dao.get(user_id)

    def get_by_name(self, name):
        # 根据name数据
        return user_dao.get_by_name(name)

    # def list(self):
    #     # 返回所有
    #     return user_dao.list()

    def save(self, user_do: UserDo):
        # 新增操作
        # 新增之前先查询数据是否存在，不存在则进行新增，存在则返回false
        user = self.get_by_name(user_do.username)
        if not user:
            return user_dao.save(user_do)
        else:
            return False

    def create_access_token(self, user_do):
        # jwt根据用户信息生成token
        return create_access_token(identity=user_do)

    @jwt.user_lookup_loader
    def user_lookup_callback(self, _jwt_header, jwt_data):
        # 获取 username
        username = jwt_data["sub"]["username"]
        # 返回通过 username 查询用户的结果
        return self.get_by_name(username)

    # def update(self, user_do: UserDo):
    #     # 修改操作
    #     # 修改之前先查询数据是否存在，存在则进行更新，不存在则返回false
    #     plan = self.get(user_do.id)
    #     if not plan:
    #         return False
    #     else:
    #         return user_dao.update(user_do)

    # def delete(self, user_id):
    #     # 删除操作
    #     # 删除之前先查询数据是否存在，存在则进行删除，不存在则返回false
    #     plan = self.get(user_id)
    #     if not plan:
    #         return False
    #     else:
    #         return user_dao.delete(user_id)
