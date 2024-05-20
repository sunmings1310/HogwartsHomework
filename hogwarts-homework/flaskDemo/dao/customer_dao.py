from typing import List

from do.customer_do import CustomerDo
from app import db_session, app


class CustomerDao:

    def get(self, customer_id) -> CustomerDo:
        # 根据id返回数据
        with app.app_context():
            return db_session.query(CustomerDo).filter_by(id=customer_id).first()

    def get_by_name(self, name) -> CustomerDo:
        # 根据name返回数据
        with app.app_context():
            return db_session.query(CustomerDo).filter_by(name=name).first()

    def list(self) -> List[CustomerDo]:
        # 返回所有数据
        with app.app_context():
            return db_session.query(CustomerDo).all()

    def save(self, customer_do: CustomerDo):
        # 新增数据
        with app.app_context():
            db_session.add(customer_do)
            db_session.commit()
            return customer_do.id

    def update(self, customer_do: CustomerDo):
        # 修改数据
        with app.app_context():
            db_session.query(CustomerDo).filter_by(id=customer_do.id).update(customer_do.as_dict())
            db_session.commit()
            return customer_do.id

    def delete(self, customer_id):
        # 删除操作
        with app.app_context():
            db_session.query(CustomerDo).filter_by(id=customer_id).delete()
            db_session.commit()
            return customer_id
