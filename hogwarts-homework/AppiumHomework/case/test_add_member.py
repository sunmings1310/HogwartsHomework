import pytest

from base.wework_app import WeworkApp
from data import get_name_and_phonenum_yaml_file


def get_datas(level):
    add_member = get_name_and_phonenum_yaml_file()["add"][level]
    add_member_datas = add_member['datas']
    add_member_idss = add_member['ids']
    return add_member_datas, add_member_idss


class TestAddMember:
    add_member_p0_datas, add_member_p0_ids = get_datas('P0')

    def setup_class(self):
        self.ww_app = WeworkApp()

    def setup(self):
        self.main = self.ww_app.start().goto_main()

    def teardown(self):
        self.ww_app.back()

    def teardown_class(self):
        self.ww_app.stop()

    @pytest.mark.parametrize("name,phone_num,expected", add_member_p0_datas, ids=add_member_p0_ids)
    def test_add_member(self, name, phone_num, expected):
        rst = self.main. \
            goto_contact(). \
            click_add_member(). \
            click_add_member_by_menual(). \
            quick_input_member_information(name, phone_num).get_add_member_rst()

        assert expected == rst
