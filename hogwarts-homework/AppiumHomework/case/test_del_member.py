import pytest

from base.wework_app import WeworkApp
from data import get_name_and_phonenum_yaml_file


def get_datas(level):
    del_member = get_name_and_phonenum_yaml_file()["del"][level]
    del_member_datas = del_member['datas']
    del_member_idss = del_member['ids']
    return del_member_datas, del_member_idss


class TestDelMember:
    del_member_p0_datas, del_member_p0_ids = get_datas('P0')

    def setup_class(self):
        self.ww_app = WeworkApp()

    def setup(self):
        self.main = self.ww_app.start().goto_main()

    def teardown(self):
        self.ww_app.back()

    def teardown_class(self):
        self.ww_app.stop()

    @pytest.mark.parametrize("name", del_member_p0_datas, ids=del_member_p0_ids)
    def test_del_member(self, name):
        name = name[0]
        search_page = self.main. \
                        goto_contact(). \
                        click_search_member().search_member_by_name(name)

        before_member_nums = search_page.get_member_nums()
        after_member_nums = search_page.\
            goto_personal_information_pgae_by_name(name).\
            goto_edit_member_page().\
            del_member_by_search().\
            get_member_nums()

        assert before_member_nums - 1 == after_member_nums
