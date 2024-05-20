from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import *

from app import db


# 创建用户表
class UserDo(db.Model):
    # 表名
    __tablename__ = "user"
    # 用例ID 用户的唯 一标识
    id = db.Column(Integer, primary_key=True)
    # 用户名, 限定 80个字符 ，不为空，并且唯一
    username = db.Column(String(80), nullable=False, unique=True)
    # 密码
    password = db.Column(String(500), nullable=False)
    # 生成时间格式, 创建时间，通常不需要手动传入，在写入记录的时候自动生成
    create_time = Column(DateTime, nullable=True, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    # 初始化操作
    def __init__(self, *args, **kwargs):
        # 密码进行自动加密
        self.username = kwargs.get('username')
        self.password = generate_password_hash(kwargs.get('password'))

    # 验证密码
    def check_hash_password(self, raw_password):
        # raw_password是传入的原始密码
        password = check_password_hash(self.password, raw_password)
        return password

    def as_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "create_time": str(self.create_time)
        }
