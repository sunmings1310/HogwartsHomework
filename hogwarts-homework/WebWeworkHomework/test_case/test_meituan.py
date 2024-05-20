import time
import random

from page_object.main_page2 import MainPage2
from page_object.wework_page import WeworkPage


class TestAddMember:
    def setup_class(self):
        #初始化主页对象
        self.main = MainPage2()
        self.main.login()

    def teardown_class(self):
        #退出driver进程
        self.main.driver.close()

    def teardown(self):
        #保证每个方法开始状态页面是正确的
        self.main.back_start_page()

    # def test_add_member(self):
    #     # 1.点击添加成员，跳转到添加成员页面
    #     # 2.add member 的操作
    #     # 3.获取通讯录页面的成员列表(成员列表)
    #     mem_list = self.main.\
    #         goto_add_member().\
    #         add_member("mingshuos8", "zhangahao", "11827423172").\
    #         get_member_list()
    #     # 4. 断言 实际结果是否符合预期
    #     time.sleep(3)
    #     assert "mingshuos7" in mem_list

    def test_goto_contact(self):
        shop_name = "药店"
        time.sleep(random.randint(30, 50))
        shop_list = self.main.goto_search().input_name(shop_name).get_shop_list()
        print(shop_list)
        # self.main.goto_contact().get_member_list()
        time.sleep(5)