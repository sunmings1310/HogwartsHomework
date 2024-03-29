import logging

import pytest


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


@pytest.fixture(scope="class", autouse=True)
def setup_class():
    # 通过 self. 让calc 变成实例变量，在用例里就可以被调用到了
    logging.debug("【开始测试】")
    yield
    logging.debug("【结束测试】")


@pytest.fixture(autouse=True)
def setup_func():
    # 每条测试用例之前调用
    logging.debug("【开始执行】")
    yield
    logging.debug("【结束执行】")

