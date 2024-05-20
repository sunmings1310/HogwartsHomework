from dao.customer_dao import CustomerDao
from do.customer_do import CustomerDo

customer_dao = CustomerDao()


class CustomerService:

    def get(self, customer_id):
        # 通过id查询数据
        return customer_dao.get(customer_id)

    def get_by_name(self, name):
        # 根据name数据
        return customer_dao.get_by_name(name)

    def list(self):
        # 返回所有
        return customer_dao.list()

    def save(self, customer_do: CustomerDo):
        # 新增操作
        # 新增之前先查询数据是否存在，不存在则进行新增，存在则返回false
        customer = self.get_by_name(customer_do.name)
        if not customer:
            return customer_dao.save(customer_do)
        else:
            return False

    def update(self, customer_do: CustomerDo):
        # 修改操作
        # 修改之前先查询数据是否存在，存在则进行更新，不存在则返回false
        is_exist = self.get(customer_do.id)
        if not is_exist:
            return False
        else:
            return customer_dao.update(customer_do)

    def delete(self, customer_id):
        # 删除操作
        # 删除之前先查询数据是否存在，存在则进行删除，不存在则返回false
        is_exist = self.get(customer_id)
        if not is_exist:
            return False
        else:
            return customer_dao.delete(customer_id)
