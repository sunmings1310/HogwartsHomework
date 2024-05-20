import time

import requests

from faker import Faker

# 后端接口的URL
url = "http://127.0.0.1:5001/customer"

# 创建Faker对象
fake = Faker('zh_CN')

num_data = 200
fake_data = []

for _ in range(num_data):
    # 定义测试数据格式
    data_format = {
        "name": fake.name(),
        "address": fake.address(),
        "age": fake.random_int(min=18, max=60),
        "birth": fake.date_of_birth().strftime("%Y-%m-%d"),
        "sex": fake.random_element(elements=("1", "2"))
    }

    fake_data.append(data_format)

for index, data in enumerate(fake_data):
    time.sleep(0.5)
    # 发送POST请求
    response = requests.post(url, json=data)
    # 检查响应状态码
    print(response.status_code)
    if response.status_code == 200:
        print(f"第{index}条数据添加成功")
    else:
        print(f"第{index}条数据添加失败")
    response.close()

# # 输出生成的测试数据
# print(fake_data)