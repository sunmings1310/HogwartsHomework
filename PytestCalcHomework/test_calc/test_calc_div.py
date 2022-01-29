import allure
import pytest
import yaml

from PytestCalcHomework.pythoncode.calculator import Calculator


# 读取 yaml 数据文件
def get_data(level):
    with open("./data/calc_datas.yml", encoding="utf-8") as f:
        result = yaml.safe_load(f)
        div_data = result.get("div")
    return div_data.get(level).get("datas"), div_data.get(level).get("ids")


@allure.feature("计算器除法模块")
class TestCalcdiv:
    div_P0_datas, div_P0_ids = get_data('P0')
    div_P1_1_datas, div_P1_1_ids = get_data('P1_1')
    div_P1_2_datas, div_P1_2_ids = get_data('P1_2')
    div_P2_datas, div_P2_ids = get_data('P2')

    def setup_class(self):
        # 通过 self. 让calc 变成实例变量，在用例里就可以被调用到了
        self.calc = Calculator()

    @pytest.mark.div
    @pytest.mark.P0
    @pytest.mark.parametrize("a,b,expect", div_P0_datas, ids=div_P0_ids)
    @allure.story("正向功能测试")
    def test_div1(self, a, b, expect):
        """
        【正向】2个数相除，结果计算正确
        :return:
        """
        with allure.step("调用计算器除法函数"):
            result = self.calc.div(a, b)
        assert result == expect

    @pytest.mark.div
    @pytest.mark.P1
    @pytest.mark.parametrize("a,b,expect", div_P1_1_datas, ids=div_P1_1_ids)
    @allure.story("有效边界值功能测试")
    def test_div2(self, a, b, expect):
        """
        【边界】有效边界值相除，结果计算正确
        :return:
        """
        with allure.step("调用计算器除法函数"):
            result = self.calc.div(a, b)
        assert result == expect

    @pytest.mark.div
    @pytest.mark.P1
    @pytest.mark.parametrize("a,b,expect", div_P1_2_datas, ids=div_P1_2_ids)
    @allure.story("无效边界值功能测试")
    def test_div3(self, a, b, expect):
        """
        【边界】无效边界值相除，展示提示信息
        :return:
        """
        with pytest.raises(eval(expect)) as e:
            with allure.step("调用计算器除法函数"):
                self.calc.div(a, b)
        # print(e.typename)
        assert e.typename == expect

    @pytest.mark.div
    @pytest.mark.P2
    @pytest.mark.parametrize("a,b,expect", div_P1_2_datas, ids=div_P1_2_ids)
    @allure.story("异常值功能测试")
    def test_div4(self, a, b, expect):
        """
        【边界】异常值相除，展示提示信息
        :return:
        """
        with pytest.raises(eval(expect)) as e:
            with allure.step("调用计算器除法函数"):
                self.calc.div(a, b)
        # print(e.typename)
        assert e.typename == expect