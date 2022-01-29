import allure
import pytest
import yaml

from PytestCalcHomework.pythoncode.calculator import Calculator


# 读取 yaml 数据文件
def get_data(level):
    with open("./data/calc_datas.yml", encoding="utf-8") as f:
        result = yaml.safe_load(f)
        add_data = result.get("add")
    return add_data.get(level).get("datas"), add_data.get(level).get("ids")

@allure.feature("计算器加法模块")
class TestCalcAdd:
    add_P0_datas, add_P0_ids = get_data('P0')
    add_P1_1_datas, add_P1_1_ids = get_data('P1_1')
    add_P1_2_datas, add_P1_2_ids = get_data('P1_2')
    add_P2_datas, add_P2_ids = get_data('P2')

    def setup_class(self):
        # 通过 self. 让calc 变成实例变量，在用例里就可以被调用到了
        self.calc = Calculator()

    @pytest.mark.add
    @pytest.mark.P0
    @pytest.mark.parametrize("a,b,expect", add_P0_datas, ids=add_P0_ids)
    @allure.story("正向功能测试")
    def test_add1(self, a, b, expect):
        """
        【正向】2个数相加，结果计算正确
        :return:
        """
        result = self.calc.add(a, b)
        assert result == expect

    @pytest.mark.add
    @pytest.mark.P1
    @pytest.mark.parametrize("a,b,expect", add_P1_1_datas, ids=add_P1_1_ids)
    @allure.story("有效边界值功能测试")
    def test_add2(self, a, b, expect):
        """
        【边界】有效边界值相加，结果计算正确
        :return:
        """
        result = self.calc.add(a, b)
        assert result == expect

    @pytest.mark.add
    @pytest.mark.P1
    @pytest.mark.parametrize("a,b,expect", add_P1_2_datas, ids=add_P1_2_ids)
    @allure.story("无效边界值功能测试")
    def test_add3(self, a, b, expect):
        """
        【边界】无效边界值相加，展示提示信息
        :return:
        """
        with pytest.raises(eval(expect)) as e:
            self.calc.add(a, b)
        # print(e.typename)
        assert e.typename == expect


    @pytest.mark.add
    @pytest.mark.P2
    @pytest.mark.parametrize("a,b,expect", add_P1_2_datas, ids=add_P1_2_ids)
    @allure.story("异常值功能测试")
    def test_add4(self, a, b, expect):
        """
        【边界】异常值相加，展示提示信息
        :return:
        """
        with pytest.raises(eval(expect)) as e:
            self.calc.add(a, b)
        # print(e.typename)
        assert e.typename == expect