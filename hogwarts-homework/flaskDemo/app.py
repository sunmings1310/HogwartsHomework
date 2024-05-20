from flask import Flask
from flask_restx import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session

app = Flask(__name__)

# 创建应用程序上下文
# app.app_context().push()

api = Api(app)
# 问题： 跨域 No 'Access-Control-Allow-Origin' header is present on the requested resource.
# 解决：
# CORS(app, supports_credentials=True)
CORS(app)
# CORS(app, resources={r'/customer': {'origins': 'http://localhost:8080'}})

# 数据库连接信息
username = "root"
password = "D3v3l0p"
server = "192.168.10.54:3307"
database = "tpf"
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{username}:{password}@{server}/{database}?charset=utf8mb4"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config["JWT_SECRET_KEY"] = "super-secret"
# JWTManager 绑定 app
jwt = JWTManager(app)
# SQLAlchemy 绑定 app
db = SQLAlchemy(app)
# 为了有类型提示所做的声明
db_session: Session = db.session
# # 这将初始化`db`对象并将其与`app`应用程序实例进行绑定。
# db.init_app(app)


def register_router():
    # 如果出现循环导入，把导包语句放在方法内执行。并且调用此函数
    # from controller.testcase_controller import testcase_ns
    # from controller.plan_controller import plan_ns
    # from controller.build_controller import build_ns
    from controller.user_controller import user_ns
    from controller.customer_controller import customer_ns
    # api.add_namespace(testcase_ns, "/testcase")
    # api.add_namespace(plan_ns, "/plan")
    # api.add_namespace(build_ns, "/build")
    api.add_namespace(user_ns, "/user")
    api.add_namespace(customer_ns, '/customer')


if __name__ == '__main__':
    register_router()
    app.run(debug=True, port=5001)