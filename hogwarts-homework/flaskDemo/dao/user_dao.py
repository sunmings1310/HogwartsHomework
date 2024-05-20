from typing import List

from do.user_do import UserDo
from app import db_session, app


class UserDao:

    def get(self, user_id) -> UserDo:
        # 根据id返回数据
        return db_session.query(UserDo).filter_by(id=user_id).first()

    def get_by_name(self, username) -> UserDo:
        # 根据username返回数据
        # print(db_session.query(UserDo))

        return db_session.query(UserDo).filter_by(username=username).first()

    def list(self) -> List[UserDo]:
        # 返回所有数据
        return db_session.query(UserDo).all()

    def save(self, user_do: UserDo):
        # 新增数据
        with app.app_context():
            db_session.add(user_do)
            db_session.commit()
            return user_do.id

    def update(self, user_do: UserDo):
        # 修改数据
        with app.app_context():
            db_session.query(UserDo).filter_by(id=user_do.id).update(user_do.as_dict())
            db_session.commit()
            return user_do.id

    def delete(self, user_id):
        # 删除操作
        with app.app_context():
            db_session.query(UserDo).filter_by(id=user_id).delete()
            db_session.commit()
            return user_id
