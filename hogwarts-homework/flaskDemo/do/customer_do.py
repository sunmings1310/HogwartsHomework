from sqlalchemy import *

from app import db


class CustomerDo(db.Model):
    # 表名
    __tablename__ = "customer"
    # 用例ID 用户的唯 一标识
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(80), nullable=False)
    addr = db.Column(String(80), nullable=False)
    age = db.Column(Integer)
    birth = db.Column(String(80))
    sex = db.Column(String(80))

    def __init__(self, *args, **kwargs):
        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
        self.addr = kwargs.get('addr')
        self.age = kwargs.get('age')
        self.birth = kwargs.get('birth')
        self.sex = kwargs.get('sex')

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "addr": self.addr,
            "age": self.age,
            "birth": self.birth,
            "sex": self.sex
        }