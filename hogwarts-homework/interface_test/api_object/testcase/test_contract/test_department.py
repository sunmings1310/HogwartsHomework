from api_object.apis.contract.department import Department
from api_object.utils.log_util import logger
from api_object.utils.utils import Utils


class TestDepartment:

    def setup(self):
        self.department_id = 588
        self.depart = Department()
        try:
            # 尝试进行定义的id的删除，排除干扰
            self.depart.delete(self.department_id)
        except Exception as e:
            logger.warning("没有待删除的部门")

    def test_create_department(self):
        assert self.depart.create(self.department_id)["errcode"] == 0
        obj = self.depart.get()
        department_list = Utils.jsonpath_util(obj, "$..department..id")
        assert self.department_id in department_list