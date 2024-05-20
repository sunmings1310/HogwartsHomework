from flask import Flask
from sqlalchemy import create_engine

app = Flask(__name__)

# 创建应用程序上下文
app.app_context().push()

username = "root"
password = "D3v3l0p"
server = "192.168.10.54:3307"
database = "tpf"
engine = create_engine(f"mysql+pymysql://{username}:{password}@{server}/{database}?charset=utf8mb4")
pool = engine.pool
print("Total connections:", pool.size())
print("Free connections:", pool.checkedin())
print("Used connections:", pool.checkedout())